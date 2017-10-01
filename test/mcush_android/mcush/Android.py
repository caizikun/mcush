# coding:utf8
__doc__ = 'mcush controller on Android'
__author__ = 'Peng Shulin <trees_peng@163.com>'
__license__ = 'MCUSH designed by Peng Shulin, all rights reserved.'
import os
import re
import sys
import time
import base64
import logging
from . import Env
from . import Utils
from . import Instrument
from . import Mcush


class QPythonBluetoothPort(Instrument.Port):
        
    UUID = '00001101-0000-1000-8000-00805F9B34FB'

    def __init__( self, parent, *args, **kwargs ):
        Instrument.Port.__init__( self, parent, *args, **kwargs )
        import androidhelper
        self.androidhelper = androidhelper
        self.android = androidhelper.Android()
 
    def connect( self ):
        if self._connected:
            return
        r = self.android.bluetoothConnect(self.UUID, self.port)
        if r.error:
            raise Instrument.SerialNotFound( self.port )
        r = self.android.bluetoothGetConnectedDeviceName('')
        print("%s Connected"% r.result)
        self._connected = True

    def disconnect( self ):
        self.android.bluetoothStop( '' )
        self._connected = False
    
    def read( self, read_bytes=1 ):
        return self.android.bluetoothRead(read_bytes, connID='').result

    def write( self, buf ):
        self.android.bluetoothWrite( buf, '' )
 
    def flush( self ):
        pass



class QMcush( Mcush.Mcush ):
    '''Mcush on Android/QPython'''
    PORT_TYPE = QPythonBluetoothPort

    def tts( self, msg ):
        self.port.android.ttsSpeak( msg )
        while True:
            r = self.port.android.ttsIsSpeaking()
            if r.result:
                time.sleep(0.5)
            else:
                break

    def vibrate( self, duration=300 ):
        self.port.android.vibrate(duration)

    def smsSend( self, addr, msg ):
        self.port.android.smsSend( addr, msg )
        


class JavaBluetoothPort(Instrument.Port):
        
    def __init__( self, parent, *args, **kwargs ):
        Instrument.Port.__init__( self, parent, *args, **kwargs )
        from jnius import autoclass
        self.UUID = autoclass('java.util.UUID')
        self.BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
        self.BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
        self.BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
        
    def connect( self ):
        if self._connected:
            return
        paired_devices = self.BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
        for device in paired_devices:
            if device.getName() == self.port:
                self.socket = device.createRfcommSocketToServiceRecord(self.UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
                #print( type(self.socket), self.socket )
                self.recv = self.socket.getInputStream()
                self.send = self.socket.getOutputStream()
                #print( type(self.recv), self.recv, type(self.send), self.send )
                self.socket.connect()
                self._connected = True
                break

    def disconnect( self ):
        self._connected = False
        self.socket.close()
    
    def read( self, read_bytes=1 ):
        ret = []
        for i in range(read_bytes):
            r = self.recv.read()
            if r:
                ret.append( chr(r) )
            else:
                break
        #print( 'read', ret )
        return ''.join(ret)

    def write( self, buf ):
        self.send.write(buf)
 
    def flush( self ):
        self.send.flush()


class KMcush( Mcush.Mcush ):
    '''Mcush on Android/Kivy'''
    PORT_TYPE = JavaBluetoothPort

    def writeCommand( self, cmd ):
        try:
            ret = Mcush.Mcush.writeCommand( self, cmd )
            print( 'cmd: ' + cmd )
            print( 'ret: ' + '\n'.join(ret) )
            return ret
        except Instrument.CommandSyntaxError:
            print( 'command syntax err: ' + cmd )
            return []

    def vibrate( self, duration=0.05 ):
        try:
            self.vibrator
        except AttributeError:
            from plyer import vibrator
            self.vibrator = vibrator
        self.vibrator.vibrate( duration )


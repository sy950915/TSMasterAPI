from TSMasterAPI import *
import threading
import inspect
import ctypes
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


# Arg[0] AObj
# Arg[1] ASocket
# Arg[2] AResult
# Arg[3] AAddr
# Arg[4] APort
# Arg[5] AData
# Arg[6] ASize
def receive_event(AObj,ASocket,AResult,AAddr,APort,AData,ASize):
    str1 = ''
    AData = cast(AData,c_char_p)
    print(f"{AAddr}:{APort}:{AData.value}")


initialize_lib_tsmaster(b"ETHUDPDemo")

tsapp_show_tsmaster_window(b"Hardware",True)


# 参数表示通道
ret = tssocket_initialize(0) 

#arg[0] ANetworkIndex
#arg[1] macaddr
#arg[2] ipaddr
#arg[3] netmask
#arg[4] gateway
#arg[5] mtu
ret= tssocket_add_device_ex(0,b'1:2:3:4:5:50', b"192.168.0.50",b"255.255.255.0", b"192.168.0.1",1500)
# 配置完成后 启动设备
ret = tsapp_connect()


# 创建Socket TCP
#arg[0] ANetworkIndex
#arg[1] AIPEndPoint
#arg[2] ASocketHandle
UDPHandle = s32(0)

ret = tssocket_udp(0,b"192.168.0.50:20001",UDPHandle)

receEvent =  TSSocketReceiveEvent_Win32(receive_event)

# 注册接收事件
tssocket_register_udp_receivefrom_event(UDPHandle,receEvent)

while 1:
    key = input("请输入:")
    if key == '1':
            # arg[0] s
            #arg[1] AData
            #arg[2] ASize
            data = (u8*1000)()
            for i in range(1000):
                data[i] = i&0xff
            ret = tssocket_udp_sendto(UDPHandle,b'192.168.0.51:30001',data,1000)
    elif key =='q':
        break



tssocket_unregister_udp_receivefrom_event(UDPHandle,receEvent)

tssocket_udp_close(UDPHandle)

tsapp_disconnect()

finalize_lib_tsmaster()




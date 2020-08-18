from django.http import JsonResponse
import json
from common.models import Devices

def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_device':
        return listdevices(request)
    elif action == 'add_device':
        return adddevices(request)
    elif action == 'modify_device':
        return modifydevices(request)
    elif action == 'del_device':
        return deletedevices(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listdevices(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Devices.objects.values()
    total  = Devices.objects.count()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist, 'total':total})

def adddevices(request):

    info    = request.params['data']

    # 从请求消息中 获取要添加设备的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Devices.objects.create(name=info['name'] ,
                            system=info['system'] ,
                            version=info['version'],
                            state=info['state'])


    return JsonResponse({'ret': 0, 'id':record.id})


def modifydevices(request):
    # 从请求消息中 获取修改设备的信息
    # 找到该客户，并且进行修改操作

    deviceid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        device = Devices.objects.get(id=deviceid)
    except Devices.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{deviceid}`的客户不存在'
        }

    if 'name' in newdata:
        device.name = newdata['name']
    if 'system' in newdata:
        device.system = newdata['system']
    if 'version' in newdata:
        device.version = newdata['version']
    if 'state' in newdata:
        device.state = newdata['state']
    # 注意，一定要执行save才能将修改信息保存到数据库
    device.save()

    return JsonResponse({'ret': 0})

def deletedevices(request):

    deviceid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Devices.objects.get(id=deviceid)
    except Devices.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{deviceid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    customer.delete()

    return JsonResponse({'ret': 0})
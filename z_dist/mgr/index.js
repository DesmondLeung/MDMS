function show_borrow_device(){
    document.getElementById("borrow_device").style.backgroundColor='#708090';document.getElementById("mange_device").style.backgroundColor='#b0c4de';
    document.getElementById("add_device_btn").style.display="none";document.getElementById("modify_device_btn").style.display="none";document.getElementById("del_device_btn").style.display="none";document.getElementById("list_device_btn").style.display="none";//隐藏
    document.getElementById("borrow_device_btn").style.display="";document.getElementById("return_device_btn").style.display="";document.getElementById("list_device_btn2").style.display="";//显

}

function show_manage_device(){
    document.getElementById("mange_device").style.backgroundColor='#708090';document.getElementById("borrow_device").style.backgroundColor='#b0c4de';
    document.getElementById("borrow_device_btn").style.display="none";document.getElementById("return_device_btn").style.display="none";document.getElementById("list_device_btn2").style.display="none";//隐藏
    document.getElementById("add_device_btn").style.display="";document.getElementById("modify_device_btn").style.display="";document.getElementById("del_device_btn").style.display="";document.getElementById("list_device_btn").style.display="";//显

}

function draw_table(json)
{
    var tr;
    for (var i = 0; i < json.length; i++) {
        tr = $('<tr/>');
        tr.append("<td>" + json[i].id + "</td>");
        tr.append("<td>" + json[i].devicename + "</td>");
        tr.append("<td>" + json[i].devicesystem + "</td>");
        tr.append("<td>" + json[i].deviceversion + "</td>");
        tr.append("<td>" + json[i].devicestate + "</td>");
        $("#list_table tbody").append(tr);
    }

}

function list_device()
{
    var httpRequest = new XMLHttpRequest();
    var url =
        'http://localhost:8000/api/mgr/devices?action=list_device&pagesize=10&&pagenum=1';
    httpRequest.open('GET', url, true);//第二步：打开连接  将请求参数写在url中  ps:"./Ptest.php?name=test&nameone=testone"
    httpRequest.send();//第三步：发送请求  将请求参数写在URL中
    /**
     * 获取数据后的处理程序
     */
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {
            var json = httpRequest.responseText;//获取到json字符串，还需解析
            console.log(json);
            var msg=eval("("+json+")");

            if(msg.ret='0' ){
                var devices = msg.retlist;
                var tb = document.getElementById('list_table');
                var rowNum=tb.rows.length;
                for (i=1;i<rowNum;i++)
                {
                    tb.deleteRow(i);
                    rowNum=rowNum-1;
                    i=i-1;
                }// 先删除旧的设备列表
                draw_table(devices)
            }

        }
    }
}


function add_device()
{

}

function modify_device()
{

}

function del_device()
{

}

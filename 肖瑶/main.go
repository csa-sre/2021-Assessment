package main

import (
	"context"
	"fmt"
	"github.com/tencentyun/scf-go-lib/cloudfunction"
	"github.com/yyz/C2Proxy/events"
	"io/ioutil"
	"net/http"
	"strings"
)

var HTTPresp *http.Response
// Run 执行
func Run(ctx context.Context, event events.APIGatewayRequest) (resp events.APIGatewayResponse, err error) {
	resp = events.APIGatewayResponse{
		IsBase64Encoded: false,
		Headers: map[string]string{},
		StatusCode: 502,
		Body: "error",
	}
	// 下面这一句replace其实是不需要的
	resqPath := strings.Replace(event.Path, "/golangTest", "", -1)
	// 下面这几行是处理QueryString
	qrString := ""
	lenQRString := len(event.QueryString)
	if lenQRString != 0 {
		qrString = "?"
		for i := range event.QueryString {
			qrString += string(i) + "=" + string(event.QueryString[i][0]) + "&"
		}
		if string(qrString[len(qrString)-1]) == "&" {
			qrString = qrString[:len(qrString)-1]
		}
	}
	// 下面开始判断是GET还是POST请求
	if event.Method == "GET" {
		HTTPresp, err = http.Get("https://www.baidu.com" + resqPath + qrString)
		if err != nil {
			resp.Body = err.Error()
			return
		}
		defer HTTPresp.Body.Close()
	} else if event.Method == "POST" {
		if event.Headers["Content-Type"] == "" {
			event.Headers["Content-Type"] = "application/x-www-form-urlencoded"
		}
		HTTPresp, err = http.Post("https://www.baidu.com" + resqPath + qrString, event.Headers["Content-Type"], strings.NewReader(event.Body))
		if err != nil {
			resp.Body = err.Error()
			return
		}
		defer HTTPresp.Body.Close()
	}


	// 下面是得到了http response 然后把他封装成API特定的返回
	// 需要封装resp.Headers、resp.StatusCode、resp.Body、resp.IsBase64Encoded
	heads := HTTPresp.Header
	for i := range heads {
		fmt.Println(heads[i])
		resp.Headers[i] = heads[i][0]
	}
	resp.StatusCode = HTTPresp.StatusCode
	content, err := ioutil.ReadAll(HTTPresp.Body)
	if err != nil {
		resp.Body = err.Error()
		return
	}
	resp.Body = string(content)
	// 下面是调试用的代码
	fmt.Println("下面是event：")
	fmt.Println(event)
	fmt.Println("结束event打印")
	fmt.Println("下面是HTTPresp URL：")
	fmt.Println("http://www.baidu.com" + resqPath + qrString)
	fmt.Println("结束HTTPresp URL打印")
	return

}


func main() {
	cloudfunction.Start(Run)
}

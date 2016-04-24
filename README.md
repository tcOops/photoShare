##阿里云ECS访问地址：
[http://139.196.199.81:8088/photos/login](http://139.196.199.81:8088/photos/public/)

##部署Requirements：
	- nginx
	- django1.8.4以上
	- django2.7以上
	- uwsgi
	- mysql

如何部署可以参考：
	[http://spacenx.pw/2015/08/20/Linux-Nginx-WSGI.html](http://spacenx.pw/2015/08/20/Linux-Nginx-WSGI.html)

##使用说明：
	-注册用户
		-先注册再登录， 不支持anonymous
		
	-登录
  		-用户登录后使用

	-登出
	
	-个人空间
		-仅用户自己可见
		-提供创建相册， 以及往相册上传照片的功能
		-上传照片之前先创建相册

	-班级相册
		-所有用户均可见
		-提供创建相册， 以及往相册上传照片的功能
		-上传照片之前先创建相册， 只能往自己创建的相册上上传照片


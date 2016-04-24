function addData(){
	var checkboxs = $('.selectNode')
	var nodeIds = ""
	var flag = false
	for(var i = 0; i < checkboxs.length; ++i){
		if(checkboxs[i].checked){
			if(flag) nodeIds += ','
			else flag = true
			nodeIds += checkboxs[i].value.toString()
		}
	}
	$('#reserveData').val(nodeIds)
}

function choseAll(){
	var checkboxs = $('.selectNode')
	for(var i = 0; i < checkboxs.length; ++i){
		checkboxs[i].checked = true
	}
}

function choseReverse(){
	var checkboxs = $('.selectNode')
	for(var i = 0; i < checkboxs.length; ++i){
		checkboxs[i].checked ^= 1
	}
}


function updateCommit(){
	routerId = 	$('#reserveRouterId').val()
	newCommit = $('#newCommits').val()
	url = "/route/updateRouterCommit/"
	data = new Object()
	data.routerId = routerId.toString()
	data.commit = newCommit
	$.ajax({
		type : 'post',
		dataType : 'json',
		url : url,
		async : true,
		data :  data,

		success : function(response){
			//Construct Data
			//console.log("ok")
			//constructNodeDetail(response[0])
		},

		error : function(response){
			console.log("Oops,  some errors !")
		}
	})
}


function showCIUser(userId){
	url = "/route/getCIUserById/"
	data = new Object()
	data.userId = userId.toString()
	$.ajax({
		type : 'post',
		dataType : 'json',
		url : url,
		async : true,
		data :  data,

		success : function(response){
			//Construct Data
			var content = '姓名  :   ' + response[1].name + '</br>'
			content += '备注  :   ' + response[1].commit + '</br>'
			content += '创建时间  :   ' + response[1].create_time
			$('#CIUserDesc').html(content)
		},

		error : function(response){
			console.log("Oops,  some errors !")
		}
	})
}

//Photos
function showPhotoSet(userId, type){
	url = "/photos/getPhotoSet/"
	data = new Object()
	data.userId = userId.toString()
	data.type = type.toString()
	$.ajax({
		type : 'post',
		dataType : 'json',
		url : url,
		async : true,
		data :  data,

		success : function(response){
			//Construct Data
		    b = response
			var content = ""

			for(var i = 0; i < b.length; ++i){
				content += "<option value='" + b[i].pk.toString() + "'> " + b[i].fields.name + " </option>"
			}
			$('#uploadSet').html(content)
		},

		error : function(response){
			console.log("Oops,  some errors !")
		}
	})
}


//Photos
function showPhotos(photoSetId){
	url = "/photos/getPhotos/"
	data = new Object()
	data.photoSetId = photoSetId.toString()
	$.ajax({
		type : 'post',
		dataType : 'json',
		url : url,
		async : true,
		data :  data,

		success : function(response){
			//Construct Data
		    b = response.photos
		    var content = ""
		    for(var i = 0; i < b.length; ++i){
		    	content += '<div class="onediv" style="text-align:center;">' 
         		content += '<span style="color:red;text-algin:center">' + b[i][1] + '</span>'
           		content += "<img src='" + b[i][0] + "' style='margin-left:0%;height:210px; width:94%'>"
          		content += '<span style="margin-top:20px;">发布于' + b[i][2] + '</span></div>'
        		if(i % 3 == 2){
        			content += '<div style="clear:both"></div> <br><br>'
        		}
		    }
		    content += '<div style="clear:both"></div> <br><br>'
		    $('#photosInfo').html(content)
		},

		error : function(response){
			console.log("Oops,  some errors !")
		}
	})
}




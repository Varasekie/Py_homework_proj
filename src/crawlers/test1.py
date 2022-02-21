s = '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>学生学习页面</title>
<link href="/css/courselist/global.css?v=20160407" rel="stylesheet" type="text/css" />
<link href="/css/courselist/play.css?v=2020-0304-1848" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css"  href="/css/courselist/face-collection-qr.css?v=2019-1019-0724"/>
<style>
.bluebtn{display:inline-block;height:28px;line-height:25px;padding:0 10px;background:#7b9e31;font-size:14px;color:#FFF;border-radius:3px;}
.bluebtn:hover{background:#8cb833;}
.AlertCon02{width:528px;height:238px;border:solid 1px #c5c5c5;background:#FFF;padding:10px}
.closed02{width:14px;height:14px;background:url(/space/new/moocIndex/images/closePng.png) no-repeat left center;margin-top:3px;}
.con03{padding:20px;text-align:center;font-size:16px;color:#202020;}
.DySearch{padding-top:15px;height:42px}
.DySearch .DySeleft{width:284px;height:28px;border:solid 1px #e1e1e1;font-size:12px;color:#555;}
.DySearch .DySeleft .Inp{width:240px;height:27px;padding:0 5px;line-height:27px;border:none;border-right:0;border-bottom:0;background:#fcfcfc;font-family:Microsoft YaHei; float:left;}
.DySearch .DySeleft .sub{width:29px;height:28px;border:none;background:url(../images/icons.png) left -116px no-repeat;cursor:pointer; float:right;}
.marTop20{margin-top:20px;}
.marTop30{margin-top:30px;}
    </style>

<script src="/js/group/baguettebox.min.js"></script>
<link rel="stylesheet" href="/css/group/baguettebox.min.css">
<link href="/css/group/chapter_common.css" type="text/css" rel="stylesheet">
<link href="/css/group/chapter_student_common.css" type="text/css" rel="stylesheet">
<link rel="stylesheet" href="/css/uploadImg.css">
<script src="/js/group/uploadNew.js?v=2019-1213-1600"></script>
<script type="text/javascript" src="/space/new/way-upload/plupload.full.min.js"></script>
<script type="text/javascript" src="/space/new/way-upload/css/DD_belatedPNG_0.0.8a-min.js"></script>
<script src="/js/group/new-chapter-group-right.js?v=2019-1220-1400"></script>
<style>#iframe{width:100%;}
#selector {
	z-index:1000;
	position:fixed;

    -khtml-user-select: none;
    -webkit-user-select: none;
    user-select: none;
}
#selector .spliter{
	height: 100%;
	top: 0;
    width: 7px;
    display: block;
    font-size: 0.1px;
    position: absolute;
    cursor: col-resize;
}
#selector .spliter.west{
	left: -5px;
}
#selector .spliter.east{
	right: -5px;
}
.mask{
	z-index:999;
	position:absolute;
	top:0;
	bottom:0;
	right:0;
	left:0;
}
.switchbtn{z-index:1001;}
.zad731{z-index:1001;}
.right{border-left:7px solid #504f55;}
.inputwords,.temptexarea{width:80%}

.iconon{background:url(/images/note/note_on.png) no-repeat;width:21px;height:21px;max-width:21px;max-height:21px;background-size:21px 21px;}
.iconoff{background:url(/images/note/note_off.png) no-repeat;width:21px;height:21px;max-width:21px;max-height:21px;background-size:21px 21px;}
.contenton{font-size: 16px;color:blue;}
.contentoff{font-size: 16px;color:#999;}
.title_block{display:inline-block;cursor:pointer}
#top {display:block;padding-right:0px;margin:10px 0;height:38px;width:51px;line-height: 36px;font-size: 16px;color: #0a0a0a;background: #fff url(/images/top.png) no-repeat 12px center;padding-left: 0px;border-radius: 3px;text-align:left;}
#kf {display:block;padding-right:0px;margin:10px 0;height:38px;width:51px;line-height: 36px;font-size: 16px;color: #0a0a0a;background: #fff url(/images/kfIcon.png) no-repeat 12px center;padding-left: 0px;border-radius: 3px;text-align:left;}
#dy {display:block;height:38px;width:51px;margin:10px 0;line-height: 36px;font-size: 16px;bottom: 210px;color: #0a0a0a;background: #fff url(/images/dyIcon.png) no-repeat 12px center;padding-left: 0px;border-radius: 3px;text-align:left;}
/*#top {position:fixed;width:76px;height:40px;line-height:40px;font-size:15px;text-align:center;bottom:144px;border:1px #e4e4e7 solid;}
#kf {position:fixed;width:76px;height:40px;line-height:40px;font-size:15px;text-align:center;bottom:102px;border:1px #e4e4e7 solid;}
.on-line-answer{position:fixed;width:76px;height:40px;line-height:40px;font-size:15px;text-align:center;bottom:62px;border:1px #e4e4e7 solid;}
*/#yj {display:block;width:26px;height:26px;margin:10px 0;background:url(/img/min_yj_22.png) no-repeat;}

/*验证码*/
.AlertCon02 {
    background: #fff none repeat scroll 0 0;
    border: 1px solid #c5c5c5;
    height: 238px;
    padding: 10px;
    width: 528px;
}
.fr{ float:right;}
.fl{ float:left;}
.clearfix {overflow:hidden;zoom:1}
.zcenter { width:600px; margin:0 auto; color:#333;margin-top: 100px;}
.zcenter a { color:#2ca4de;}

.zc_h2 { padding-top:50px; font-size:36px;}
/*.zc_table { margin-top:35px;}*/
.zc_table{width:334;text-align: left;}
.zc_table td {padding-top:11px;font-size: 16px;}
.zc_table  td span.sp_h2{font-size: 16px;}
.zc_name {text-align:right;width: 85px;}
.zc_table td.zc_vercode_ac{font-size: 12px;vertical-align: middle;padding-left: 0px;}
img{vertical-align: middle;}
.zc_input330,.zc_input32 { width:325px; height:28px; padding-left:5px; border:1px #d7d7d7 solid; border-radius:3px; background:none; line-height:28px;}
.zc_input32 { width:155px;}
.zc_verify { padding:0px;margin:0px;padding-right: 5px;padding-left: 7px;}
.zc_btn,.zc_btn1 { display:inline-block; padding-top:10px; font-size:20px; text-align:center;}
.zc_btn a ,.zc_btn1 a{ display:inline-block; width:163px; height:30px; border-radius:4px; line-height:30px; text-align:center; background-color:#7B9E31; color:#fff;}
.zc_btn a:hover ,.zc_btn1 a:hover { background-color:#6e850c; text-decoration:none;}
.zc_old { padding-left:10px;}
.zc_fontsize1 { padding-top:43px; color:#555; font-size:22px;}
.zc_fontsize2 { padding-top:10px; padding-bottom:40px; color:#555; font-size:14px;}
.zgray ,zgray a {color:gray}
.zgreen ,.zgreen a { color:#839b1b;}
.zc_ps { width:400px; margin:0 auto;  margin-top:32px; padding-top:26px; padding-left:28px; padding-right:26px; border-top:1px #ccc solid; text-align:left; font-size:14px; }
.zc_ps a { color:#2ca4de;}
.zc_p { line-height:24px;}
.zwindow { width:547px; height:341px; margin:0 auto; border:1px #ccc solid; border-radius:3px; text-align:left;}
.zw_left { font-size:18px; text-align:left;}
.zw_title { height:57px; padding-left:18px; background-color:#839b1b; line-height:57px; font-size:18px; color:#fff; }
.zw_box { padding:30px; font-size:14px; line-height:24px;}
.zw_content { height:185px;}
.swfupload{float:left;}
.role{color:#0367b0;font-size:12px;}
.openlock{display:none;color:#7b9e31;cursor:pointer;text-decoration:underline;cursor: pointer;height: 30px;margin-top: -15px; position: absolute; right: 45px;top: 300px;width: 60px;}
.bigImgDiv{position:fixed;top:0;left:0;width:100%;height:100%;display:none;z-index:999999;}
.bigImgMask{position:absolute;top:0;left:0;width:100%;height:100%;background:#000;opacity:0.8;z-index:1000001;}
.bigImgClose{position:absolute;top:26px;right:52px;width:26px;height:26px;background:url(/images/closeImgView.png) no-repeat left center;background-size:100%;z-index:1000002;}
.bigImgDiv img{position:absolute;left: 0;right: 0;top: 0;bottom: 0;margin:auto;z-index:1000003;display:inline-block;max-height: 80%;}

.teacherTool{position:absolute;width:84px;z-index:99999;bottom:84px;display:none;}
#btnOpt{float:right;padding:0 10px;border:1px solid #7b9e31;position:relative;}
.toolOpenBtn{width:11px;height:36px;position:absolute;top:70%;z-index:100;}
.toolCloseBtn{width:11px;height:36px;position:absolute;top:50%;margin-top:-18px;}
.jobhint{width:45px;height:45px;border-radius:32px;background:#ff9838;position:absolute;bottom:260px;}
	.chapterQrcode{left:0px;}
	.teacherTool{left:318px;}
    .toolOpenBtn{right:-11px;background:url(/images/toolOpenLeftBtn.png)}
    .toolCloseBtn{right:-11px;background:url(/images/toolCloseLeftBtn.png) no-repeat left center;}
    .jobhint{right:-100px;}
.zad71{
    width:42px;
    height:23px;
    background: #9BA;
    position:fixed;
    top: 159px;
    right: 111px;
    color:green;
    text-align:center;
    font-size:10pt;
    display:none;
    margin-right: 10px;
    padding-left: 15px;
    padding-right: 15px;
    line-height: 24px;
    border-radius: 4px;
    color: green;
}
</style>
<script src="/js/ServerHost.js"></script>
<script type="text/javascript" src="/js/courselist/jquery-1.7.2.min.js"></script>
<script src="/js/jquery.color.js"></script>
<script type="text/javascript" src="/static/js/domain.js"></script>
<script type="text/javascript" src="https://fystat-ans.chaoxing.com/log/setlog?personid=106370187&courseId=209185064&classId=18563006&encode=d65ca0683664c826c9dd9db0dd527122&chapterId=271487172"></script>
<script src="/space/new/js/wayer_v1.2.mini.js" ></script>
<script src="/js/check_vercode.js" type="text/javascript"></script>
<script type="text/javascript">
window['dtype'] =  "Course";
window['app'] =  "0";
var ua=navigator.userAgent.indexOf('chaoxing_wisdomclass');
if(ua!=-1){
	document.write('<script src="/js/phone/protocolChaoXing/CXJSBridge.js"><\/script>');
	document.write('<script src="/js/phone/app.utils.js?v=1"><\/script>');
}
var utEnc="c4430bd1faa65e210af159a3c44bc56f";
var courseId=209185064;
var courseid=209185064;
String.prototype.trim=function(){return this.replace(/(^\s*)|(\s*$)/g,"");}
//设置cookie
var setCookie = function(name,value,hours,path,domain) {
	var oNow = new Date();
	oNow.setHours(oNow.getHours() + hours);
	var sCookie = name + "=" + escape(value);

	if(hours) {
		sCookie += ";expires=" + oNow.toGMTString();
	}

	if(path) {
		sCookie += ";path=" + path;
	}

	if(domain) {
		sCookie += ";domain=" + domain;
	}

	document.cookie = sCookie;
};


//获取cookie
var getCookie = function(name) {
	var oRegExp = new RegExp("(^|)" + name + "=([^;]*)(;|$)","gi").exec(document.cookie), aCookie;
	if(aCookie = oRegExp) {
		return unescape(aCookie[2]);
	}
	return null;
};

var showorhide=function(htmlid){
	var doc = document.getElementById(htmlid);
	if(doc!=null){
    	if(doc.style.display!="none"){
    		doc.style.display="none";
    	}else{
    		doc.style.display="block";
    	}
	}
};

var show=function(htmlid){
	var doc = document.getElementById(htmlid);
	doc.style.display="block";
};
var tasckvalidate=function(clazzid,nodeid){
	    window.open("/edit/validate?clazzid="+clazzid+"&nodeid="+nodeid+"&courseId="+courseId);
};

function bindSubCheck(callback) {
	$('#sub').unbind('click');
	$('#sub').on('click', function() {
    	var code=$("#code").val();
    	jQuery.ajax({
    		   type:"POST",
    		   url:"/kaptcha-img/ajaxValidate2",
			   data:{code:code},
    		   success: function(data){
    			 $("#code").val("");
				 if(data.status){
					 $("#validate").css("display","none");
					 WAY.box.hide();
					 var enc=data.enc;
					// $("#enc").val(enc);
					 callback && callback(enc);
					 //flushfinish(code,nodeid,clazzid);getVarCode
				 }else{
					 getVarCode();
					 //location.href="/edit/validate?nodeid="+nodeid+"&clazzid="+clazzid
				 }
    		   }
    	});
    });
}

function validateTime(classId, courseId, callback) {
	jQuery.ajax({
		type : "GET",
		url : "/work/validate",
		cache : false,
		data : {
			classId : classId,
			courseId : courseId
		},
		success : function(data) {
			if (data.status == 1) {
				alert("账号发生异常，请重新登录！");
				return;
			}
			if (data.status == 2) {
				// 弹出验证码
				getVarCode();   //重新请求,防止缓存
				WAY.box.show({
					'divid' : 'validate',
					bkcolor : 'none'
				});
				bindSubCheck(callback);
			}
			if (data.status == 3) {
				callback && callback('', '');
			}
		}
	});
}

 $(document).ready(function(){

	jQuery.ajax({ //一个Ajax过程
			type: "get", //以get方式与后台沟通
			url : "/mycourse/studentstudycourselist",
			dataType:'html',//返回的值
			data: {courseId:'209185064',chapterId:'271487172',clazzid:'18563006'},
			success: function(data){//如果调用成功
    		    document.getElementById("coursetree").innerHTML=data;
                		jQuery(".ncells h4").removeClass();
        				jQuery(".ncells h5").removeClass();
						jQuery(".ncells .flush").css('display','none');
			            jQuery("#cur"+'271487172').parent().parent().find(".flush").css('display','block');
			            var bulletFormat = "";
						if( bulletFormat != "null" && bulletFormat == "Dot"){
						  $(".hideChapterNumber").hide();
						}
						$(".knowledgeOpenBtn").click();
						$(".knowledgeOpenBtn").removeClass("knowledgeOpenCurBtnImg");
						jQuery(".ncells h4").removeClass();
        				jQuery(".ncells h5").removeClass();
						jQuery("#cur"+'271487172').addClass("currents");
						checkMobileBrowerLearn();
			}
		});
});
		$(".ncells h4").live('click',function(){
    		jQuery(".ncells h4").removeClass("currents");
			jQuery(".ncells h5").removeClass("currents");
    		jQuery(this).addClass("currents");
			jQuery(".ncells .flush").css('display','none');
			jQuery(this).parent().parent().find(".flush").css('display','block');
    	})
		$(".ncells h5").live('click',function(){
    		jQuery(".ncells h4").removeClass("currents");
			jQuery(".ncells h5").removeClass("currents");
			jQuery(".ncells .flush").css('display','none');
    		jQuery(this).addClass("currents");
			jQuery(this).parent().parent().find(".flush").css('display','block');
    	})
    	function getJobCount(obj) {
			var knowledgeJobCount = $(obj).find(".jobUnfinishCount");
			var totalCount = 0;
			for (var i = 0; i < knowledgeJobCount.size(); i++) {
				var singleJobCount = parseInt(knowledgeJobCount.eq(i).val());
				totalCount += singleJobCount;
			}
			return totalCount;
		}
    	$(".knowledgeOpenBtn").live('click', function(event){
    		event.stopPropagation();
		var flag = $(this).parent().parent().hasClass("cells");
		if ($(this).parent().next("div").css("display") == "block") {
			$(this).removeClass("knowledgeOpenBtnImg");
			$(this).removeClass("knowledgeOpenCurBtnImg");
			$(this).addClass("knowledgeCloseBtnImg");
			if (flag) {
				$(this).parent().parent().find("div").css("display", "none");
				$(this).parent().parent().find(".knowledgeOpenBtn").removeClass("knowledgeOpenBtnImg").addClass("knowledgeCloseBtnImg");
			} else {
				var nextDiv = $(this).parent().nextAll("div");
				nextDiv.find("div").css("display","none");
				nextDiv.css("display", "none");
				nextDiv.find(".knowledgeOpenBtn").removeClass("knowledgeOpenBtnImg").addClass("knowledgeCloseBtnImg");
				var jobTotalCount = getJobCount($(this).parent().parent());
				if ($(this).parent().find(".jobUnfinishCount").size() != 0) {
					// 当前章节任务点个数不为0
					$(this).parent().find(".jobCount").text(jobTotalCount);
				} else {
					// 当前章节任务点个数为0，子章节中任务点个数不为0
					if (jobTotalCount != 0) {
						$(this).parent().find(".roundpointStudent").addClass("orange01").text(jobTotalCount);
						$(this).parent().find(".roundpoint").addClass("orange01").text(jobTotalCount);
					}
				}
			}
		} else {
			$(".knowledgeOpenBtn").removeClass("knowledgeOpenCurBtnImg");
			$(this).removeClass("knowledgeCloseBtnImg");
			$(this).addClass("knowledgeOpenBtnImg");
			$(this).addClass("knowledgeOpenCurBtnImg");
			if (flag) {
				// 点击单元控制收缩按钮获取二级目录下的任务点个数
				var leveltwo = $(this).parent().parent().children("div.ncells");
				for (var i = 0, len = leveltwo.size(); i < len; i++) {
					var levelTwoItem = leveltwo.eq(i);
					var jobTotalCount = getJobCount(levelTwoItem);
					var orange = levelTwoItem.children(":not('div')").find(".jobCount");
					// 当子章节的任务点个数为0并且存在小黄球的时候
					if (orange.size() != 0) {
						orange.text(jobTotalCount);
					} else {
						if (jobTotalCount != 0) {
							levelTwoItem.children(":first").find(".noJob").addClass("orange01").text(jobTotalCount);
						}
					}
				}
				// 控制单元下二级目录显示
				leveltwo.show();
			} else {
				// 获取点击的章节元素
				var curKnowledgeJobCount = $(this).parent().find(".jobUnfinishCount");
				if (curKnowledgeJobCount.size() != 0) {
					var curJobCount = curKnowledgeJobCount.val();
					curJobCount = parseInt(curJobCount);
					$(this).parent().find(".jobCount").text(curJobCount);
				} else {
					$(this).parent().find(".roundpointStudent").removeClass("orange01").text("");
					$(this).parent().find(".roundpoint").removeClass("orange01").text("");
				}
				// 获取子章节div
				var nextDiv = $(this).parent().nextAll("div");
				for (var i = 0, len = nextDiv.size(); i < len; i++) {
					var nextItemDiv = nextDiv.eq(i);
					var jobTotalCount = getJobCount(nextItemDiv);
					var orange = nextItemDiv.children(":not('div')").find(".jobCount");
					// 当子章节的任务点个数为0并且存在小黄球的时候
					if (orange.size() != 0) {
						orange.text(jobTotalCount);
					} else {
						if (jobTotalCount != 0) {
							nextItemDiv.children(":first").find(".noJob").addClass("orange01").text(jobTotalCount);
						}
					}
				}
				nextDiv.show();
			}
		}
	})
var addDiscussReply = function(discussId,replycount){

 	var doc = document.getElementById("discuss"+discussId);
 	var content = doc.value;
	if(content==null||content=='')
	{
		alert("内容不能为空！");
		return;
	}
	/*if(content.length>300){
		alert("字数不能超过300");
		doc.value = title.substring(0,300);
		return;
	}*/
	doc.value = "";
	jQuery.post("/bbsapi/addDiscussReply",
    	{
			discussId : discussId
    		,replycount : replycount
    		,clazzid : '18563006'
    		,userId : '116148942'
    		,content : content
			,role : 1
    		,schoolId : '2815',
			replaytype:'1',
			ut:'s'
    	},
        function(data){
    		if(data=='error'){
    			alert("添加失败！");
    		}else{
			   var doc = document.getElementById("replaylist"+discussId);
        	   data = data.replace(/(^\s*)|(\s*$)/g,"");
			   doc.innerHTML = data;
			   var rcdoc = document.getElementById("replycount"+discussId);
			   rcdoc.innerHTML = parseInt(rcdoc.innerHTML)+1;
			   //alert("操作成功！");
			   //showorhide("replaytextarea"+discussId);
    		}
		}
	);
 };


var replay = function(num,disid,schoolid) {
		var doc = document.getElementById("replaylist"+disid);
		var showeddoc = document.getElementById("showed"+disid);
		if(doc.style.display!="none"){
			doc.style.display = "none";
			//showeddoc.innerHTML="显示";
		}else{
			var obj = doc.innerHTML;
			if(obj==null||obj==""){

			     jQuery.post("/schoolCourseInfo/getReplayList",
			    	{
						discussid:disid,
						schoolId:schoolid,
						replycount:num,
						date:new Date(),
						replaytype:'1'
			    	},
			        function(data){
			    		data = data.replace(/(^\s*)|(\s*$)/g,"");
			    		doc.innerHTML = data;
					}
				);
			     //showeddoc.innerHTML="隐藏 ";
			     doc.style.display = "block";
				 show("replaytextarea"+disid);
			}else{
				//showeddoc.innerHTML="隐藏 ";
				doc.style.display = "block";
				show("replaytextarea"+disid);
			}
		}
};

var praise = function(obj,disid,schoolid) {
 	 jQuery("#praise"+disid).removeClass();
     jQuery("#praise"+disid).addClass("cur");
	jQuery.post("/schoolCourseInfo/addBBSPraise",
    	{
			 disid:disid
			,schoolid : schoolid
			,userid:'116148942'
    	},
        function(data){
		   var doc = document.getElementById("praise"+disid);
		   doc.innerHTML = parseInt(doc.innerHTML)+1;
		   obj.onclick=null;

		}
	);

}

 var addtopcomment = function(clazzid){
 	var title = document.getElementById("toplevelTextCommentTitle").value;
	if(title==null || title=='' || title.trim()=='')
	{
		alert("标题不能为空！");
		return;
	}
	if(title.length>50){
		alert("字数不能超过50");
		document.getElementById("toplevelTextCommentTitle").value = title.substring(0,50);
		return;
	}

 	var content = document.getElementById("toplevelTextCommentContent").value;
	/*
	if(content==null||content=='')
	{
		alert("内容不能为空！");
		return;
	}
	if(content.length>300){
		alert("字数不能超过300");
		document.getElementById("toplevelTextCommentContent").value = title.substring(0,300);
		return;
	}*/
	//title=escape(encodeURI(title));
	document.getElementById("toplevelTextCommentTitle").value = "";

	//content=escape(encodeURI(content));
	document.getElementById("toplevelTextCommentContent").value = "";

	var ask = 0;
	if(document.getElementById("askteacher") != null){
    	if(document.getElementById("askteacher").checked == true){
    		ask=1;
    	}
	}
    var chapterId = document.getElementById("chapterIdid").value;
	jQuery.post("/bbsapi/addCDiscuss",
    	{
		   moocId:'209185064',
		   clazzid:'18563006',
		   userId:'116148942',
		   title: title,
		   content:content,
		   chapterIds:chapterId,
		   schoolId:'2815',
		   replaytype:'1',
		   ask : ask,
		   role:'1'
		   ,type: 'student'
		   ,ut:'s'
    	},
        function(data){
		   data = data.replace(/(^\s*)|(\s*$)/g,"");
		   var doc = document.getElementById("content2");
		   doc.innerHTML = data;
			//alert("操作成功！");
		}
	);
 };
 function getcookie(objname){
	var arrstr = document.cookie.split("; ");
	for(var i = 0;i < arrstr.length;i ++){
		var temp = arrstr[i].split("=");
		if(temp[0] == objname){
			return unescape(temp[1]);
		}
	}
}
function getChapterRightDiscuss(){
    var chapterId=document.getElementById("chapterIdid").value;
	//jQuery.post("/schoolCourseInfo/getChapterRightDiscuss",
	jQuery.post("/schoolCourseInfo/getgrouptopic",
	    {
			courseId:'209185064'
			,clazzid:'18563006'
			,type: 2
			,ut:'s'
			,chapterId:chapterId
    	},
        function(data){
    	   data = data.replace(/(^\s*)|(\s*$)/g,"");
		   var doc = document.getElementById("content2");
		   doc.innerHTML = data;
		    $(function(){
                bindImg2('fileUploader_group');
				baguetteBox.run('.smallImg', {
  					animation: 'fadeIn',
					});
            });

			$(function(){
					$(".newTopic0").click(function(){
					down();
				})
			})
		}
	);
}

function getGroupChapterRightDiscuss(){

	//jQuery.post("/schoolCourseInfo/getChapterRightDiscuss",
	jQuery.post("/schoolCourseInfo/getgrouptopic",
    	{
			courseId:'209185064'
			,clazzid:'18563006'
			,type: 2
			,ut:'s'
   		},
        function(data){
  	   	data = data.replace(/(^\s*)|(\s*$)/g,"");
		   var doc = document.getElementById("content2");
		   doc.innerHTML = data;
		}
	);
}

var changePan = function(num){
	num = parseInt(num);
    var check = checkUnsave();
    if(num != 3 && check){
        return;
	}
	for(var i=1;i<=3;i++){
		var titledoc = document.getElementById("tit"+i);
		var contentdoc = document.getElementById("content"+i);
		if(1!=0||(1==0&&i!=2)){
    		if(i==num){
    			titledoc.className="current01";
    			titledoc.style.display="block";
    			contentdoc.style.display="block";
    		}else{
    		    titledoc.className="";
    			contentdoc.style.display="none";
    		}
		}
	}
}

function saveOr(isave){
	 if(isave == 1){
		 addOrUpdateClazzNote();
	 }else{
		 var writenotecontent = $("#writenotecontent");
		 writenotecontent.empty();
	 }
	 $("#noSaveTips").css('display','none');
}

var changeDisplayContent = function(num,totalnum,chapterId,courseId,clazzid,knowledgestr){
		num = parseInt(num);
		totalnum = parseInt(totalnum);
    PCount.setIndex(num);
    	for(var i=1;i<=totalnum;i++){
    		var titledoc = document.getElementById("dct"+i);
    		var leftdoc = document.getElementById("left"+i);
    		var rightdoc = document.getElementById("right"+i);
    		if(i==num){
    			titledoc.className="c"+i+" currents";
    			leftdoc.style.display="block";
    			rightdoc.style.display="block";
            	num = num-1;
				document.getElementById("iframe").src="/knowledge/cards?clazzid="+clazzid+"&courseid="+courseId+"&knowledgeid="+chapterId+"&num="+num+"&ut=s&cpi=106370187&v=20160407-1";
    			var el = $('#iframe');
    			window.ed_reinitIframe = function ed_reinitIframe(){
    				var iframe = el[0];

    				try{
    					var bHeight = iframe.contentWindow.document.body.scrollHeight;
    					var dHeight = iframe.contentWindow.document.documentElement.scrollHeight;
    					var height = Math.max(bHeight, dHeight);
    					el.attr('height',height);
    				}catch (ex){}
    			}
				//var openlockdiv=document.getElementById("openlock");
				if($("#openlock").length>0){
                    if(num+1==totalnum){
    					setTimeout('openlockshow();',2000);
    				}else{
    					document.getElementById("openlock").style.display="none";
    				}
				}
    			window.setInterval("ed_reinitIframe()", 200);
				//jobflagOperation();

    		}else{
    		    titledoc.className="c"+i;
    			leftdoc.style.display="none";
    			rightdoc.style.display="none";
    		}
    	}
		if(typeof(MoocPlayers)!='undefined'){

			 MoocPlayers.clearMids();
		}

}

var PCount = (function () {
    var cur = 1, inner = changeDisplayContent;

    return {
        setIndex : function (index) {
            cur = index;
        },
        next : function (count, chapterId, courseId, clazzid, knowledgestr) {
            cur = parseInt(cur);
            count = parseInt(count);
            if (cur >= count) {
                document.getElementById("mainid").innerHTML = "<div style=\"width:32px;height:32px;margin:0 auto;padding:300px 0\"><img src=\"/images/courselist/loading.gif\" /></div>"
                cur = 1;
                jQuery.post("/mycourse/changeCapter",
                        {
                            courseId : courseId
                            , clazzid : clazzid
                            , chapterId : chapterId
                            , knowledgestr : knowledgestr
                            , type : 1
                            , date : new Date()
                        },
                        function (data) {
                            //alert(20160407);
                            data = data.replace(/(^\s*)|(\s*$)/g, "");
                            var doc = document.getElementById("mainid");
                            jQuery(doc).html(data);
                            chapterId = document.getElementById("chapterIdid").value;
                            jQuery(".ncells h4").removeClass();
                            jQuery(".ncells h5").removeClass();
                            jQuery("#cur" + chapterId).addClass("currents");
                            jQuery(".ncells .flush").css('display', 'none');
                            jQuery("#cur" + chapterId).parent().parent().find(".flush").css('display', 'block');
                            var el = $('#iframe');

                            window.ed_reinitIframe = function ed_reinitIframe() {
                                var iframe = el[0];

                                try {
                                    var bHeight = iframe.contentWindow.document.body.scrollHeight;
                                    var dHeight = iframe.contentWindow.document.documentElement.scrollHeight;
                                    var height = Math.max(bHeight, dHeight);
                                    el.attr('height', height);
                                } catch (ex) {
                                }
                            }
                            // var openlockdiv=document.getElementById("openlock");
                            if ($("#openlock").length > 0) {
                                var count = document.getElementById("cardcount").value;
                                if (count == 1) {
                                    setTimeout('openlockshow();', 2000);
                                }
                            }

                            if ($("#cur" + chapterId + " .orange01").length > 0) {

                                jQuery.ajax({
                                    type : "get",
                                    url : "/edit/validatejobcount",
                                    data : {
                                        courseId : courseId
                                        , clazzid : clazzid
                                        , nodeid : chapterId
                                    },
                                });
                            }

                            window.setInterval("ed_reinitIframe()", 200);
                            //jobflagOperation();
                            getClazzNote();
                        }
                );
            } else {
                cur++;
                inner(cur, count, chapterId, courseId, clazzid, knowledgestr);

            }
            scroll(0, 0);
        },
        previous : function (count, chapterId, courseId, clazzid, knowledgestr) {
            cur = parseInt(cur);
            count = parseInt(count);
            if (cur <= 1) {
                document.getElementById("mainid").innerHTML = "<div style=\"width:32px;height:32px;margin:0 auto;padding:300px 0\"><img src=\"/images/courselist/loading.gif\" /></div>"
                cur = 1;
                jQuery.post("/mycourse/changeCapter",
                        {
                            courseId : courseId
                            , clazzid : clazzid
                            , chapterId : chapterId
                            , knowledgestr : knowledgestr
                            , type : 0
                            , date : new Date()
                        },
                        function (data) {
                            data = data.replace(/(^\s*)|(\s*$)/g, "");
                            var doc = document.getElementById("mainid");
                            jQuery(doc).html(data);
                            chapterId = document.getElementById("chapterIdid").value;
                            jQuery(".ncells h4").removeClass();
                            jQuery(".ncells h5").removeClass();
                            jQuery("#cur" + chapterId).addClass("currents");
                            jQuery(".ncells .flush").css('display', 'none');
                            jQuery("#cur" + chapterId).parent().parent().find(".flush").css('display', 'block')
                            var el = $('#iframe');

                            window.ed_reinitIframe = function ed_reinitIframe() {
                                var iframe = el[0];

                                try {
                                    var bHeight = iframe.contentWindow.document.body.scrollHeight;
                                    var dHeight = iframe.contentWindow.document.documentElement.scrollHeight;
                                    var height = Math.max(bHeight, dHeight);
                                    el.attr('height', height);
                                } catch (ex) {
                                }
                            }
                            // var openlockdiv=document.getElementById("openlock");
                            if ($("#openlock").length > 0) {
                                var count = document.getElementById("cardcount").value;
                                if (count == 1) {
                                    setTimeout('openlockshow();', 2000);
                                }
                            }

                            if ($("#cur" + chapterId + " .orange01").length > 0) {

                                jQuery.ajax({
                                    type : "get",
                                    url : "/edit/validatejobcount",
                                    data : {
                                        courseId : courseId
                                        , clazzid : clazzid
                                        , nodeid : chapterId
                                    },
                                });
                            }

                            window.setInterval("ed_reinitIframe()", 200);
                            //jobflagOperation();
                            getClazzNote();
                        }
                );
            } else if (cur > 0) {
                cur--;
                inner(cur, count, chapterId, courseId, clazzid, knowledgestr);
            }
            scroll(0, 0);
        }
    }
})();

function showChapterVerificationCodeTip(){
    closeChapterVerificationCode();
    var width = $(document).width()-$('#selector').width();
    WAY.box.show({ 'divid' : 'chapterVerificationCodeTip'});
    $('.wmask').width(width);
}

function showChapterVerificationCode(){
    var width = $(document).width()-$('#selector').width();
    WAY.box.show({ 'divid' : 'chapterVerificationCode'});
    $('.wmask').width(width);
    chapterVerifyCode();
}

function  closeChapterVerificationCode(){
    if($('.wmask').length == 0){
       return;
    }
    WAY.box.hide();
    $('#chapterVerificationCode').css('display','none');
    $('#chapterVerificationCodeTip').css('display','none');
}

function chapterVerifyCode() {
    try {
        var identifyCodeRandom = $("#identifyCodeRandom");
        if (identifyCodeRandom) {
            identifyCodeRandom.val("");
        }
    } catch (e) {}
    $("img[name='chapterNumVerCode']").attr("src", "/verifyCode/studychapter?" + new Date().getTime());
}

function recordCheckedChapterParam(courseId,clazzid,chapterId,cpi){
    if(!window.checked_chapter_param){
        window.checked_chapter_param =  {} ;
    }
    checked_chapter_param.courseId = courseId;
    checked_chapter_param.clazzid = clazzid;
    checked_chapter_param.chapterId = chapterId;
    checked_chapter_param.cpi = cpi;
}

function continueGetTeacherAjax(){
    var courseId = checked_chapter_param.courseId ;
    var  clazzid = checked_chapter_param.clazzid ;
    var chapterId =  checked_chapter_param.chapterId ;
    var cpi = checked_chapter_param.cpi ;
    var identifyCodeRandomObj = $("#identifyCodeRandom");
    var chapterVerCode = identifyCodeRandomObj.val();
    if(chapterVerCode == ''){
       identifyCodeRandomObj.animate({
            backgroundColor : 'pink'
        }, 1000, function() {
            identifyCodeRandomObj.animate({
                backgroundColor : '#fcfcfc'
            }, 500, null);
        });
        return;
    }
    getTeacherAjax(courseId,clazzid,chapterId,cpi,chapterVerCode);
}

function getTeacherAjax(courseId, clazzid, chapterId, cpi, chapterVerCode) {
    closeChapterVerificationCode();
    if (courseId == 0 || clazzid == 0 || chapterId == 0) {
        alert("无效的参数！");
        return;
    }
    if (typeof (cpi) == 'undefined') {
        cpi = 0;
    }
    document.getElementById("mainid").innerHTML = "<div style=\"width:32px;height:32px;margin:0 auto;padding:300px 0\"><img src=\"/images/courselist/loading.gif\" /></div>"
    jQuery.post("/mycourse/studentstudyAjax",
            {
                courseId : courseId
                , clazzid : clazzid
                , chapterId : chapterId
                , cpi : cpi
                , verificationcode : chapterVerCode || ''
            },
            function (data) {
                data = data.replace(/(^\s*)|(\s*$)/g, "");
                var doc = document.getElementById("mainid");
                jQuery(doc).html(data);
                var el = $('#iframe');
                if ($("#openlock").length > 0) {
                    var count = document.getElementById("cardcount").value;
                    if (count == 1) {
                        setTimeout('openlockshow();', 2000);
                    }
                }
                if ($("#cur" + chapterId + " .orange01").length > 0) {

                    jQuery.ajax({
                        type : "get",
                        url : "/edit/validatejobcount",
                        data : {
                            courseId : courseId
                            , clazzid : clazzid
                            , nodeid : chapterId
                        },
                    });
                }
                window.ed_reinitIframe = function ed_reinitIframe() {
                    var iframe = el[0];

                    try {
                        var bHeight = iframe.contentWindow.document.body.scrollHeight;
                        var dHeight = iframe.contentWindow.document.documentElement.scrollHeight;
                        var height = Math.max(bHeight, dHeight);
                        el.attr('height', height);
                    } catch (ex) {
                    }
                }
                window.setInterval("ed_reinitIframe()", 200);

                var tab =0;
                if (tab == 3) {
                    getClazzNote();
                    changePan('3');
                } else if (tab == 2) {
                    getChapterRightDiscuss();
                    changePan('2');
                } else {
                    changePan('1');
                }
            }
    );
    window.setInterval("setposition()", 200);

    //jobflagOperation();

    scroll(0, 0);
}

var getMouseX = function(event) {
	event = event || window.event;
	return event.pageX || (event.clientX + (document.documentElement.scrollLeft || document.body.scrollLeft));
};

$(function () {
	var oMain = jQuery('.main').first();
	var oSelector = jQuery('#selector');
	var oWestSpliter = jQuery('#selector .spliter.west').first();
	var oEastSpliter = jQuery('#selector .spliter.east').first();
	var iMinWidth = 303;
	var sMask = '<div class="mask"></div>';

	oWestSpliter.on('mousedown', function(event) {

		event = event || window.event;

		var iX = getMouseX(event);
		var iWidth = oSelector.innerWidth();

		oWestSpliter[0].setCapture && oWestSpliter[0].setCapture();

		oMain.append(sMask);

		jQuery(document).bind('mousemove', function(ev) {
			ev = ev || window.event;

			var iDX = getMouseX(ev) - iX;
			var iToWidth = iWidth - iDX;

			if (iToWidth < iMinWidth) {
				return;
			}

			setCookie('selectwidth', iToWidth, 24 * 7, '/mycourse/studentstudy');
			oSelector.css('width', iToWidth + 'px');
		});

		jQuery(document).bind('mouseup', function() {
			oWestSpliter[0].releaseCapture && oWestSpliter[0].releaseCapture();
			var oMask = jQuery('.mask').first();
			oMask && oMask.remove();
			jQuery(document).unbind('mousemove');
			jQuery(document).unbind('mouseup');
		});
	});

	oEastSpliter.on('mousedown', function(event) {
		event = event || window.event;

		var iX = getMouseX(event);
		var iWidth = oSelector.innerWidth();

		oEastSpliter[0].setCapture && oEastSpliter[0].setCapture();

		oMain.append(sMask);

		jQuery(document).bind('mousemove', function(ev) {
			ev = ev || window.event;

			var iDX = getMouseX(ev) - iX;
			var iToWidth = iWidth + iDX;

			if (iToWidth < iMinWidth) {
				return;
			}

			setCookie('selectwidth', iToWidth, 24 * 7, '/mycourse/studentstudy');
			oSelector.css('width', iToWidth + 'px');
		});

		jQuery(document).bind('mouseup', function() {
			oEastSpliter[0].releaseCapture && oEastSpliter[0].releaseCapture();
			var oMask = jQuery('.mask').first();
			oMask && oMask.remove();
			jQuery(document).unbind('mousemove');
			jQuery(document).unbind('mouseup');
		});
	});
});

</script>


<script type="text/javascript">
function jobflag(){
	var ff = window.frames[0];
	var jobNum = 0,finishedNum =0;
	if(ff){
		jobNum += jQuery(".ans-job-icon",ff.document).size();
        finishedNum += jQuery(".ans-job-finished",ff.document).size();
	}
	if(jobNum > 2 && jobNum - finishedNum > 0){
		jQuery("#jobhint").fadeIn();
		jQuery("#jobhint span").html(jobNum - finishedNum);

		var unfinished = jQuery(".ans-job-icon",ff.document).parent().not(".ans-job-finished");

    	if(unfinished.size()>0){
			jQuery("#jobhint").attr("href","javascript:;");
			jQuery("#jobhint").click(function(){
				//var tar = jQuery(unfinished[0]);
				//console.log(tar);
				//jQuery("html,body").animate({scrollTop:tar.offset().top},200);
				jQuery("html,body").animate({scrollTop:jQuery(jQuery(".ans-job-icon",window.frames[0].document).parent().not(".ans-job-finished")[0]).offset().top},200);
			});
    	}else{
    		jQuery("#jobhint").attr("href","javascript:;");
    		jQuery("#jobhint span").html(0);
    		$("#jobhint").unbind("click");
    	}

	}else{
		jQuery("#jobhint").fadeOut();
		jQuery("#jobhint").attr("href","javascript:;");
		jQuery("#jobhint span").html(0);
		$("#jobhint").unbind("click");
	}
}

function jobflagOperation(){
    try{
    	setTimeout(jobflag,6000);
    }catch(e){console.log(e.message);}
}

// jQuery(document).ready(function(){
// 	setTimeout(jobflag,5000);
// });

</script>

</head>
<body>
<div class="bigImg"><img src=""></div>
	<div class="imgBg"></div>
<a name="gotop"></a>
<div class="zad729">
<div class="content">

            <div class="goback"><span></span> <a href="javascript:void(0)"onclick="goback()">回到课程</a></div>
    
    <div class="main" id="mainid"></div>

</div>
</div>


<div class="zad730 ui-widget-content" id="selector" >
<div class="tabs">
<div class="lists">
    <ul>
                    <li id="tit1" onclick="changePan('1');" class="current01">目录</li>
            <li id="tit2" class=""  onclick="getChapterRightDiscuss();changePan('2');">讨论</li>            <li id="tit3" class=""  onclick="getClazzNote();changePan('3');">笔记</li>
            </ul>
    <div class="clear"></div>
</div>

 <div class="showcontent">
 <div class="thiscontent chapter" style="display:block" id="content1">
	<div class="onetoone" id="coursetree">
    </div>
 </div>
    <div class="thiscontent discuss" id="content2" style="display : none"></div>
    <div id="content3" class="thiscontent note" style="display:none">
        <h3 style="display: none"><span style="float:left"></span>
			                <a style="float:right;margin-top:5px;color:#7b9e31;font-size:12px;cursor: pointer;" onclick="addOrUpdateClazzNote();" >
                    <span style="display:inline-block;width:54px;height:20px;line-height:20px;border:1px #7b9e31 solid;border-radius:2px; text-align:center;">保存</span>
                </a>
			        </h3>
		        <div class="kc_notes">
            <div class="kc_notes_botton">
                <div class="kc_notes_title"><h2><b></b>已创建笔记</h2><a style="font-size: 12px">&nbsp;&nbsp;刷新后展示新发布笔记</a><a class="kc_notes_upDown" id="kc_notes_upDown" href="#">收起</a></div>
                <div class="kc_notes_wod" id="no_notes">本章您还没有创建过笔记...</div>
                <div class="kc_notes_list" id="kc_notes_list">
                </div>
            </div>

            <div class="kc_notes_padding">
                <div class="kc_notes_title"><h2><b></b>发布笔记</h2></div>
                <div class="kc_notes_form">
                    <div class="kc_notes_area" contenteditable="true" id="writenotecontent"></div>
                    <div class="kc_notes_bnt"><input type="button" name="" onclick="addOrUpdateClazzNote()" value="保存" /></div>
                </div>
            </div>
        </div>

        <div class="maskLayer" style="display:none;"></div>
        <div class="pop_notes" id="noSaveTips"style="display:none;">
            <div class="pop_notes_title"><h2>提示</h2><a class="pop_notes_dele" href="#"></a></div>
            <div class="pop_notes_content">
                <p>您还有章节笔记未保存，是否保存？</p>
            </div>
            <div class="pop_notes_bnt">
                <a class="pop_bnt_blue" href="javascript:void(0)" onclick="saveOr(1)">保存</a>
                <a class="pop_bnt_gray" href="javascript:void(0)" onclick="saveOr(0)">不保存</a>
            </div>
        </div>
		        <div id="successTip"  class="zad71">
            已保存        </div>
        <div id="errorTip"  class="zad71">
        </div>
    </div>
</div>
</div>
	<div style="" class="teacherTool">
		<div id="btnOpt">
						                                    	<div class="toolCloseBtn"></div>
		</div>
	</div>
	<a href="#" id="jobhint" class="jobhint" style="display:none;">
		<span style="display:block;width:45px;height:45px;text-align:center;font-size:20px;line-height:45px;color:#fff;">0</span>
	</a>
	<div class="spliter west" style="z-index: 90;width:7px;height:29px;position:absolute;top:40%;left:-7px;"><img src="/images/Rtiao.png"></div>
	<div class="spliter east" style="z-index: 90;"></div>
	<div class="toolOpenBtn"></div>
</div>
<div class="zad731"></div>
<div style="height: 100%;display:none;" id="messagedialogepar" class="bgmask">
</div>
<div style="margin-top: -255.5px;" class="mypop" id="messagedialoge"></div>
<div class="AlertCon02" id="validate" style="width:368px;height:139px;display:none;" align="center" >
    <table class="zc_table">
	    <tr>
           <td colspan="3">
			<span class="sp_h2">请输入验证码：</span>
			</td>
      </tr>
	  <tr>
        <td colspan="2">
			<input class="zc_input32" name="code" id="code" type="text"
					onkeydown="keydownSubmit(event)"
					onfocus="hiddenError('mod_error')"/>
        </td>
		<td class="zc_vercode_ac">
				<span class="zc_verify" onclick="getVarCode();">
				<img src="/kaptcha-img/code" width="124" height="28" id="imgVerCode"/></span>
				<a href="javascript:void(0);" onclick="getVarCode();" style="color:#02bffd">看不清</a>
		</td>
      </tr>
      <tr>
        <td colspan="2" style="text-align: left;">
			<span class="zc_btn">
				<a href="javascript:void(0);" id="sub">确定</a>
			</span>
		</td>
        <td></td>
      </tr>
    </table>
</div>
<div class="bigImgDiv">
	<div class="bigImgMask"></div>
	<div class="bigImgClose"></div>
</div>
<!-- 人脸采集  -->
    
<!-- 章节验证码  -->
<div style="width:385px;height:auto;display:none;" class="AlertCon02" id="chapterVerificationCode">
    <h3 class="clearfix"><a class="closed02 fr" href="javascript:void(0)" onclick="closeChapterVerificationCode();"></a></h3>
    <div class="con03">
        <p style="margin-right: 78px;font-size: 15px;">为保障您的账号安全，请输入验证码</p>
        <div class="marTop20"></div>
        <div class="DySearch" style="width:303px;padding-left:16px;" id="randomIdentifyCodeInp">
            <div class="DySeleft fl" style="border:none;">
                <input type="text"  class="Inp fl" id="identifyCodeRandom" name="identifyCodeRandom" style="width:138px;border:1px solid #ccc;border-radius:4px;" placeholder="请输入验证码" vlaue="" autofocus = "autofocus">
                <img src="/verifyCode/studychapter" class="fl" width="93" height="28" name="chapterNumVerCode" style="display: block; position: absolute; left: 210px;" onclick="chapterVerifyCode()"/>
                <a href="javascript:" onclick="chapterVerifyCode()" style="float:right; font-size: 9pt; color: #7b9e31; text-decoration: underline;line-height:30px;">看不清</a>
            </div>
        </div>
        <div class="marTop30" id="startTestDiv">
            <a class="bluebtn"  href="javascript:void(0)" onclick="continueGetTeacherAjax();">继续学习</a>
        </div>
    </div>
</div>

<!-- 章节验证码--提示框  -->
<div style="width:385px; height:144px;display:none;" class="AlertCon02" id="chapterVerificationCodeTip">
    <h3 class="clearfix"><a class="closed02 fr" href="javascript:void(0)" onclick="WAY.box.hide();$('#chapterVerificationCodeTip').css('display','none');showChapterVerificationCode();" ></a></h3>
    <div class="con03">
        <p id="tipIdentifyCode">验证码不正确，请重新输入</p>
        <div class="marTop30">
            <a class="bluebtn" href="javascript:void(0)" onclick="WAY.box.hide();$('#chapterVerificationCodeTip').css('display','none');showChapterVerificationCode();">确定</a>
        </div>
    </div>
</div>

</body>
<script type="text/javascript" src="/js/courselist/tabs.js?v=20160407"></script>
<script type="text/javascript" src="/js/courselist/recognize.js?v=20160407"></script>
<script type="text/javascript" src="/js/courselist/inputDefault.js?v=20160407"></script>
<script type="text/javascript" src="/js/courselist/player.js?v=20160407"></script>
<script type="text/javascript" src="/js/courselist/util.js?v=20160407"></script>
<script src="/js/chapterDiscussUploadCourseImg.js?v=2018-0130-1400"></script>
<script src="/js/swfupload/swfupload.js"></script>
<script type="text/javascript" src="/js/swfupload/swfupload.queue.js"></script>
<link href="/css/courselist/popwin.css?v=20160407" rel="stylesheet" type="text/css" />
<link href="/css/note/chapterNote.css" rel="stylesheet" type="text/css" />
<script type="text/javascript">
var pid = getCookie('pid');//得到联盟id即pid
//如果是安徽联盟，则隐藏联系客服
if(pid != undefined && pid == 348){
	$("#isAhlm").hide();
}
//如果是无锡职业技术学院-控制技术学院，则隐藏联系客服
var fid = getCookie('fid');
if(fid != undefined && fid == 159){
	$("#isAhlm").hide();
}

$(document).ready(function(){
function setwidth(){
	if(screen.width <= 1024){$('.switchbtn').click();}

	var selectwidth = getCookie('selectwidth');

	if (selectwidth) {
		jQuery('#selector').css('width', selectwidth + 'px');
	}
}
setwidth();
    $('.kc_notes_upDown').on('click',function(){
        var _this = $(this).parent().next().next();
        if(_this.is(':visible')){
            _this.slideUp(200)
            $(this).text('展开')
        }else{
            _this.slideDown(200)
            $(this).text('收起')
        }
    })
    var notesBox = $('.kc_notes').parent().innerHeight()
    $('.kc_notes').css('height',notesBox)
    $('.maskLayer').css('height',$(document).innerHeight())
    $('.pop_notes').css('top',($(window).innerHeight()-$('.pop_notes').innerHeight())/2)
});
var onReadComplete =function(){
   setTimeout('onReadComplete1();',6000);
}

var onReadComplete1 =function(){
   if(!document.getElementById("chapterIdid")){
        return;
   }
   var chapterId = document.getElementById("chapterIdid").value;
   var closeLists = jQuery(".knowledgeCloseBtnImg");
   var idLists = "";
   for (var i = 0, len = closeLists.size(); i < len; i++) {
	   var id = closeLists.eq(i).parent().attr("id");
	   idLists += id + ",";
   }
   idLists = idLists.substring(0, idLists.length - 1);

	jQuery.ajax({ //一个Ajax过程
			type: "get", //以get方式与后台沟通
			url : "/mycourse/studentstudycourselist",
			dataType:'html',//返回的值
			data: {courseId:'209185064',chapterId:chapterId,clazzid:'18563006'},
			success: function(data){//如果调用成功
    		    document.getElementById("coursetree").innerHTML=data;
				jQuery(".ncells .flush").css('display','none');
			    jQuery("#cur"+chapterId).parent().parent().find(".flush").css('display','block');
			    var bulletFormat = "";
				if( bulletFormat != "null" && bulletFormat == "Dot"){
					$(".hideChapterNumber").hide();
				}
				$(".knowledgeOpenBtn").click();
				$(".knowledgeOpenBtn").removeClass("knowledgeOpenCurBtnImg");
				jQuery(".ncells h4").removeClass();
				jQuery(".ncells h5").removeClass();
	            jQuery("#cur"+chapterId).addClass("currents");
	            var array = idLists.split(",");
	            for (var i = 0, len = array.length; i < len; i++) {
	            	if (jQuery("#" + array[i]).find(".knowledgeOpenBtn").hasClass("knowledgeCloseBtnImg")) {
	            		continue;
	            	}
	            	jQuery("#" + array[i]).find(".knowledgeOpenBtn").click();
	            }
			}
		});

	//setTimeout(jobflag,1000);
}
function addZero(num) {
  if (num < 10) {
    return '0' + num;
  }

  return num;
}
function dateFormate(second){
    if(second<=0){
    	return "00:00:00";
    }else{
    	var date = new Date(second * 1000);
			var h = date.getHours() - 8;
			var m = date.getMinutes() ;
			var s = date.getSeconds();
			var ts = addZero(h) + ':' + addZero(m) + ':' + addZero(s);
		return ts;
    }

}

function conversion(times){
    // 比如需要这样的格式 yyyy-MM-dd hh:mm:ss
    var date = new Date(times);
    Y = date.getFullYear() + '-';
    M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
    D = (date.getDate()+1 < 10 ? '0'+(date.getDate()+1) : date.getDate()+1)+' ';
    h = date.getHours() + ':';
    m = date.getMinutes() + ':';
    s = date.getSeconds();
    return Y+M+D+h+m+s;
   // 输出结果：2014-04-23 18:55:49
}

function checkUnsave(){
  var writenotecontent = $("#writenotecontent");
    if(writenotecontent.html() != '' && writenotecontent.html() != ""){
        $("#noSaveTips").css('display','block');
       return true;
    }
    return false;
}

function getClazzNote(){
    //获取章节笔记列表
    var chapterId = document.getElementById("chapterIdid").value;

    jQuery.ajax({
        type : "get",
        url : "/schoolCourseInfo/chapternotelist",
        data : {
            userid:116148942,
            chapterId:chapterId,
            courseId : 209185064
        },
		success: function(data){
            if(data != null){
                data = jQuery.parseJSON(data);
                if(data.result == 1){
                    $("#kc_notes_list").css('display','block');
                    $("#no_notes").css('display','block');
                    $("#kc_notes_upDown").css('display','inline');


                    if(data.data.list.length > 0){
                        $("#no_notes").css('display','none');
                        var kc_notes_list =  $("#kc_notes_list");
                        kc_notes_list.empty();
                        var content = null;
                        var createTime = null;
                        var cid = null;
                        var array = data.data.list;
                        for(var i = 0 ; i<array.length;i++){
                            var json = array[i];
                            $.each(json, function(i) {
                                if(i == 'content'){
                                    content = json[i];
                                }else if(i == 'createTime'){
                                    createTime = conversion(json[i]);//得到的结果是2012-10-12 22:37:33
                                } else if(i == 'cid') {
                                    cid = json[i];
                                }
                            });
                            kc_notes_list.append('<dl class="kc_notes_row">\n' +
                                    '                        <dt><a target="_blank" href="http://note.yd.chaoxing.com/pc/note_note/noteDetailLatest/'+cid+'">'+content+'...</a></dt>\n' +
                                    '                        <dd>创建日期：'+createTime+'</dd>\n' +
                                    '                    </dl>');
                        }
                    }else{
                        $("#kc_notes_list").css('display','none');
                        $("#kc_notes_upDown").css('display','none');
                    }
                }
			}

		}
    });
};

function goback(){
   if(checkUnsave()){
      return;
   }
    window.location.href = "/mycourse/studentcourse?courseId=209185064&clazzid=18563006&enc=cba80d78eb4605ded056492337b5dc7d";
}
var isblank=false;
getTeacherAjax('209185064','18563006','271487172','106370187');
var lsatNoteContent="";

    var addOrUpdateClazzNote = function(){
	   try{
			$("#writenotecontent > p").each(function(){
    			var pvalude= $(this).text().replace(/(^\s*)|(\s*$)/g,'').replace(/<br[^>]*>/gi, '<br>');
    			if (pvalude.trim() == '<br>') {
        			$(this).text("");
        		}
    			if(pvalude.trim().length==0){
    				$(this).remove();
    			}
    		})

		}catch(e){
		}

		//去除p跟从时间点p的样式
		try{
			$("#writenotecontent > p").each(function(){
				if($(this).find('img').size()==0){
					$(this).css('color','#000000');
				}
    		})

		}catch(e){
		}

    	var content = $("#writenotecontent").html();
    	if(content=='null'||content==null||content=='undefined'){
    		return ;
    	}

    	try{
    		var temp = content.replace(/(^\s*)|(\s*$)/g,'').replace(/<br[^>]*>/gi, '<br>');
    		if (temp.trim() == '<br>') {
    			content = '';
    	 		$("#writenotecontent").html(content);
    		}
			content=content.replace(/(^\s*)|(\s*$)/g,'');
			content=content.replace(/(&nbsp;)*$/g,'');
			if(content.length==0&&isblank){
				return;
			}
			isblank=false;

    	}catch(e) {
    	}
		if(lsatNoteContent == content){
    	 	return ;
    	}
    	lsatNoteContent = content;
		var chapterId = document.getElementById("chapterIdid").value;
		jQuery.ajax({
    			type: "post",
    			url : "/schoolCourseInfo/newNote/add",
    			dataType:'html',
    			data: {
            			userid : '116148942',
            			content : content,
    					courseName:'高等数学BⅡ',
                        chapterId:chapterId,
                        courseId : 209185064
    				},
    			success: function(data){
                   var jsonObject = jQuery.parseJSON(data);
                   if(jsonObject.status){
                       if(content.length==0){
                           isblank=true;
                       }
                       $("#successTip").fadeIn().delay(1200).fadeOut(100);
                       $("#writenotecontent").empty();
				   }else{
                       $("#errorTip").html(jsonObject.msg);
                       $("#errorTip").fadeIn().delay(1200).fadeOut(100);
				   }
        		   return data;
    			}
    		});
	}
	function getNotePidShow(){
		$("#writenotecontent > p").each(function(){
			try{
				var oAtitle= $(this).children('span')[0];
				oAtitle.setAttribute("class","title_block");
				oAtitle.setAttribute("contenteditable","false");

    			oAtitle.onmouseover = function(){
					$(this.getElementsByTagName('img')[0]).removeClass('class');
					this.getElementsByTagName('img')[0].setAttribute('class', 'iconon');
					this.getElementsByTagName('img')[0].setAttribute('src', '/images/note/note_on.png');
					$(this.getElementsByTagName('span')[0]).removeClass('class');
					this.getElementsByTagName('span')[0].setAttribute('class', 'contenton');
					$("#writenotecontent").attr('contenteditable',false);
				}
				oAtitle.onmouseout = function(){
					$(this.getElementsByTagName('img')[0]).removeClass('class');
					this.getElementsByTagName('img')[0].setAttribute('class', 'iconoff');
					this.getElementsByTagName('img')[0].setAttribute('src', '/images/note/note_off.png');
					$(this.getElementsByTagName('span')[0]).removeClass('class');
					this.getElementsByTagName('span')[0].setAttribute('class', 'contentoff');
					$("#writenotecontent").attr('contenteditable',true);
				}
			}catch(e){
			}
		})
	}
function down(){
	var el = $('.newPic'),
    curHeight = el.height(),
    autoHeight = el.css('height', 'auto').height();
    el.height(curHeight).animate({height: autoHeight}, 250);
}

function openlockshow(){
	if($("#openlock").length>0){
		document.getElementById("openlock").style.display="block";
	}
}

function openLock(count,chapterId,courseId,clazzid,knowledgestr){
	jQuery.get("/edit/openlock",
    	{
			clazzid : clazzid,
			nodeid : chapterId,
			courseId:courseId
    	},
        function(data){
			if(data=="true"){
				PCount.next(1,chapterId,courseId,clazzid,knowledgestr);
				onReadComplete();
			}
		}
	);
}
function clickImg(){
	$("#iframe").contents().find("img:not(.content-banner img)").click(function(){
		var imgSrc = $(this).attr("src");
        var originImg = '<img src=' + imgSrc + '>';
		$(".bigImgDiv").css("display","block");
		$(".bigImgDiv").append(originImg);
    })
    }
$(".bigImgClose").click(function(){
	$(".bigImgDiv").css("display","none");
	$(".bigImgDiv img").remove();
})
	$(".toolOpenBtn").click(function() {
		$(".teacherTool").show();
	})
	$(".toolCloseBtn").click(function() {
		$(".teacherTool").hide();
	})
</script>

<script type="text/javascript">
			(function() {
				var backToTopTxt = "返回顶部", backToTopEle = $('<a title="返回顶部" id="top"  style="left:327px;"  href="javascript:scroll(0,0)" target="_self"></a>').appendTo($("#btnOpt"))
					.attr("title", backToTopTxt).click(function() {
						$("html, body").animate({ scrollTop : 0 }, 520);
				}), backToTopFun = function() {
					var st = $(document).scrollTop(), winh = $(window).height();
					(st > 0)? backToTopEle.show(): backToTopEle.hide();
					//IE6下的定位
					if (!window.XMLHttpRequest) {
						backToTopEle.css("top", st + winh - 60);
					}
				};
				$(window).bind("scroll", backToTopFun);
				$(function() { backToTopFun(); });
			})();
		</script>

<script>
(function(){
var script = document.createElement("script"),
	url = "http://passport2.chaoxing.com/api/passport2-onlineinfo.js?key=true&refer=http://i.mooc.chaoxing.com",
	url = url.replace("http://", window.location.protocol+"//");
script.setAttribute("type", "text/javascript");
script.setAttribute("src", url);
document.documentElement.appendChild(script);
})()
</script>
  <script>

_=~[];_={___:++_,$$$$:(![]+"")[_],__$:++_,$_$_:(![]+"")[_],_$_:++_,$_$$:({}+"")[_],$$_$:(_[_]+"")[_],_$$:++_,$$$_:(!""+"")[_],$__:++_,$_$:++_,$$__:({}+"")[_],$$_:++_,$$$:++_,$___:++_,$__$:++_};_.$_=(_.$_=_+"")[_.$_$]+(_._$=_.$_[_.__$])+(_.$$=(_.$+"")[_.__$])+((!_)+"")[_._$$]+(_.__=_.$_[_.$$_])+(_.$=(!""+"")[_.__$])+(_._=(!""+"")[_._$_])+_.$_[_.$_$]+_.__+_._$+_.$;_.$$=_.$+(!""+"")[_._$$]+_.__+_._+_.$+_.$$;_.$=(_.___)[_.$_][_.$_];_.$(_.$(_.$$+"\""+"("+_.$$$$+_._+"\\"+_.__$+_.$_$+_.$$_+_.$$__+_.__+"\\"+_.__$+_.$_$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+"(){\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.$$$$+"\\"+_.__$+_.$_$+_.$$_+_._$_+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+_.$$$$+_._+"\\"+_.__$+_.$_$+_.$$_+_.$$__+_.__+"\\"+_.__$+_.$_$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+"(){\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$__+_.$$$+_.$$$_+_.__+"\\"+_.__$+_.___+_._$$+_._$+_._$+"\\"+_.__$+_.$_$+_._$$+"\\"+_.__$+_.$_$+_.__$+_.$$$_+"(\\\"_"+_._+"\\"+_.__$+_.$_$+_.__$+_.$$_$+"\\\");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"\\"+_.$__+_.___+"("+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+"==\\"+_.__$+_.$_$+_.$$_+_._+(![]+"")[_._$_]+(![]+"")[_._$_]+"||"+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+"=="+_._+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+_.$$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$$_+_.$$_$+")\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_._$_+_.$$$_+_.__+_._+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.$$_+";\\"+_.$__+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+"=\\\"\\\"+"+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.__+_.$_$_+"\\"+_.__$+_.$__+_.$$$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+_.$$_$+_._$+_.$$__+_._+"\\"+_.__$+_.$_$+_.$_$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.__+".\\"+_.__$+_.$__+_.$$$+_.$$$_+_.__+"\\"+_.__$+_.___+_.$_$+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$_$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.__+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.___+_._$_+"\\"+_.__$+_.$$$+_.__$+"\\"+_.__$+_._$_+_.$__+_.$_$_+"\\"+_.__$+_.$__+_.$$$+"\\"+_.__$+_.__$+_.$$_+_.$_$_+"\\"+_.__$+_.$_$+_.$_$+_.$$$_+"('\\"+_.__$+_.$$_+_._$$+_.$$__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$$_+_.___+_.__+"'),\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+(![]+"")[_._$_]+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"[],\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_._$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"{},\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$$+(![]+"")[_._$_]+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+_.$$$$+_._+"\\"+_.__$+_.$_$+_.$$_+_.$$__+_.__+"\\"+_.__$+_.$_$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+"(\\"+_.__$+_.$$_+_._$$+"){\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"},\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$$_+_.$$$+".\\"+_.__$+_.$_$+_.$$_+_.$$$_+"\\"+_.__$+_.$$$+_.___+_.__+"\\"+_.__$+_._$_+_.__$+_._+_.$$$_+"\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$_$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+"||\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$$_+_.$$$+"."+_.$_$_+_._+_.__+"\\"+_.__$+_.$_$+_.___+_._$+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$$$+_._$_+_.$$$_+"\\"+_.__$+_.___+_._$$+"\\"+_.__$+_.$_$+_.___+_.$$$_+_.$$__+"\\"+_.__$+_.$_$+_._$$+"\\"+_.__$+_.$$_+_._$$+"||\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$$_+_.$$$+"."+_.$_$_+_._+_.__+"\\"+_.__$+_.$_$+_.___+_._$+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$$$+_._$_+_.$$$_+"\\"+_.__$+_.___+_._$$+"\\"+_.__$+_.$_$+_.___+_.$$$_+_.$$__+"\\"+_.__$+_.$_$+_._$$+"||(\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$$_+_.$$$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+_._$+"\\"+_.__$+_.$_$+_.$_$+_.$$$_+"&&\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$$_+_.$$$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+_._$+"\\"+_.__$+_.$_$+_.$_$+_.$$$_+"."+_.$_$_+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$$_+_._$$+"&&\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$$_+_.$$$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+_._$+"\\"+_.__$+_.$_$+_.$_$+_.$$$_+"."+_.$_$_+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$$_+_._$$+".\\"+_.__$+_.$$_+_._$_+_.$$$_+"\\"+_.__$+_.$_$+_.$_$+_._$+"\\"+_.__$+_.$$_+_.$$_+_.$$$_+"\\"+_.__$+_.___+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$$$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+_.$$$_+")||($(\\\"#"+_.__+_._$+"\\"+_.__$+_.__$+_.$$_+_.$$$_+"\\"+_.__$+_.$$$+_.___+_.__+"\\\")&&$(\\\"#"+_.__+_._$+"\\"+_.__$+_.__$+_.$$_+_.$$$_+"\\"+_.__$+_.$$$+_.___+_.__+"\\\")."+_.__+_.$$$_+"\\"+_.__$+_.$$$+_.___+_.__+"()!=\\\"\\\");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$_$+"\\"+_.__$+_.$_$+_.$_$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$$_+_.$$$+"."+(![]+"")[_._$_]+_._$+_.$$__+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+".\\"+_.__$+_.$_$+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+_.__+".\\"+_.__$+_.$$_+_._$_+_.$$$_+"\\"+_.__$+_.$$_+_.___+(![]+"")[_._$_]+_.$_$_+_.$$__+_.$$$_+"(/^.+?\\\\./,\\\"\\\");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$$+_._$+"\\"+_.__$+_.$$_+_._$_+"(\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"="+_.___+";\\"+_.__$+_.$_$+_.__$+"<"+_.__+_.$_$_+"\\"+_.__$+_.$__+_.$$$+"\\"+_.__$+_.$$_+_._$$+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+";\\"+_.__$+_.$_$+_.__$+"++){\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+_.__+_.$_$_+"\\"+_.__$+_.$__+_.$$$+"\\"+_.__$+_.$$_+_._$$+"[\\"+_.__$+_.$_$+_.__$+"].\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$$_+_._$_+_.$$__+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"("+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"('\\"+_.__$+_.$_$+_.___+_.__+_.__+"\\"+_.__$+_.$$_+_.___+"://')>="+_.___+"\\"+_.$__+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"&&\\"+_.$__+_.___+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"("+_.$$_$+"\\"+_.__$+_.$_$+_.$_$+")<"+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"&&\\"+_.$__+_.___+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"(\\\"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$_$+_.$_$+"."+_.$_$$+_.$_$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+_._+"."+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$_$+"/\\\")<"+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"&&\\"+_.$__+_.___+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"(\\\"\\"+_.__$+_.$$_+_.__$+"\\"+_.__$+_.$$_+_.__$+"."+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$_$+"/\\\")<"+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"&&\\"+_.$__+_.___+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"(\\\"\\"+_.__$+_.$$_+_._$$+_._$+"\\"+_.__$+_.$__+_.$$$+_._$+_._+"."+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$_$+"/\\\")<"+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"&&\\"+_.$__+_.___+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"(\\\"\\"+_.__$+_.$_$+_.$_$+_.$$$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$_$+_._$+_.__+_._+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+"."+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$_$+"/\\\")<"+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"&&\\"+_.$__+_.___+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"(\\\"\\"+_.__$+_.$$_+_._$$+_._$+"\\"+_.__$+_.$__+_.$$$+_._$+_._+"."+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$_$+"/\\\")<"+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"&&\\"+_.$__+_.___+_.__+".\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.__$+_.__$+_.$$$+_.$$$$+"(\\\"\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$$$+_.___+"-\\"+_.__$+_.$_$+_.$_$+_.$$$_+_.$$_$+"\\"+_.__$+_.$_$+_.__$+_.$_$_+"."+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$_$+"/\\\")<"+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"){\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_._$+"["+_.__+"]="+_.__$+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.$__+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$$+_._$+"\\"+_.__$+_.$$_+_._$_+"(\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.__+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.$__+_.___+_._$+"){\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+(![]+"")[_._$_]+".\\"+_.__$+_.$$_+_.___+_._+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$_$+_.___+"("+_.__+");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"("+(![]+"")[_._$_]+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+">"+_.___+"||"+_.$$$$+"\\"+_.__$+_.$_$+_.$$_+"){\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"\\"+_.$__+_.___+"("+_.$$$$+"\\"+_.__$+_.$_$+_.$$_+")\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$$_+_.___+_._+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\\"<\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$$_+_.___+_._+_.__+"\\"+_.$__+_.___+_.__+"\\"+_.__$+_.$$$+_.__$+"\\"+_.__$+_.$$_+_.___+_.$$$_+"=\\\\\\\"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$_$+_.__$+_.$$_$+_.$$_$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\\\\\\"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+(![]+"")[_._$_]+_._+_.$$$_+"=\\\\\\\""+_.$__$+_.$_$+_._$_+_.$$$+"\\\\\\\">\\\";\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.$_$_+"\\"+_.__$+_.$__+_.$$$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_.$$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$__+_.$$$+_.$_$_+_.__+_._$+"\\"+_.__$+_.$$_+_._$_+"."+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.___+_.__$+"\\"+_.__$+_.$__+_.$$$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.__+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.__+_.$$$_+"\\"+_.__$+_.$$$+_.___+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$$$+_.__$+"\\"+_.__$+_.$$_+_.___+_.__+"("+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+"\\"+_.$__+_.___+"+\\\"|\\\"\\"+_.$__+_.___+"+\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$$_+_.___+_._+_.__+","+_._+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.$$_$+");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"$."+_.$_$_+"\\"+_.__$+_.$_$+_._$_+_.$_$_+"\\"+_.__$+_.$$$+_.___+"({\\"+_.$__+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_._+"\\"+_.__$+_.$$_+_._$_+(![]+"")[_._$_]+":\\\"/\\"+_.__$+_.$_$+_.$_$+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_._$$+_.$$$_+_.$$_$+"/\\"+_.__$+_.$_$+_.$$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$_$_+"\\\",\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$_$+_.$_$_+_.__+_.$_$_+":{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.__+_.$$$_+"\\"+_.__$+_.$$$+_.___+_.__+"\\"+_.$__+_.___+":\\"+_.$__+_.___+_.__+_.$$$_+"\\"+_.__$+_.$$$+_.___+_.__+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"},\\"+_.$__+_.___+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.__+"\\"+_.__$+_.$$$+_.__$+"\\"+_.__$+_.$$_+_.___+_.$$$_+":'\\"+_.__$+_.$$_+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+_.__+"'\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"});\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"};\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_._$$+_.$$$_+_.__+"\\"+_.__$+_._$_+_.$__+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$_$+_.$$$_+_._$+_._+_.__+"("+_.$$$$+"\\"+_.__$+_.$_$+_.$$_+_._$_+","+_.__$+_.___+_.___+_.___+_.___+");\\"+_.__$+_._$_+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+_.$$$$+_._+"\\"+_.__$+_.$_$+_.$$_+_.$$__+_.__+"\\"+_.__$+_.$_$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$$$+_.__$+"\\"+_.__$+_.$$_+_.___+_.__+"(\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+",\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_.$$$+_.$$_$+")\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"\\"+_.$__+_.___+"(\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_.$$$+_.$$_$+"\\"+_.$__+_.___+"==\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$$_+_._+(![]+"")[_._$_]+(![]+"")[_._$_]+"\\"+_.$__+_.___+"||\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_.$$$+_.$$_$+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+"\\"+_.$__+_.___+"<=\\"+_.$__+_.___+_.___+")\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_._$_+_.$$$_+_.__+_._+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$$_+_._+(![]+"")[_._$_]+(![]+"")[_._$_]+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\\"\\\";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$$+_._$+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"(\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+_.___+";\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.$__+_.___+"<\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_.$$$+_.$$_$+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+";\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"++)\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"+=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_.$$$+_.$$_$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.___+_._$$+_._$+_.$$_$+_.$$$_+"\\"+_.__$+_.___+_.__$+_.__+"(\\"+_.__$+_.$_$+_.__$+")."+_.__+_._$+"\\"+_.__$+_._$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+"();\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_._$_+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.__$+_.$_$+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.___+"."+_.$$$$+(![]+"")[_._$_]+_._$+_._$+"\\"+_.__$+_.$$_+_._$_+"(\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+"\\"+_.$__+_.___+"/\\"+_.$__+_.___+_.$_$+");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$_$+_._+(![]+"")[_._$_]+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.__$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.__+"(\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.___+_.__$+_.__+"(\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_._$_+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+")\\"+_.$__+_.___+"+\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.___+_.__$+_.__+"(\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_._$_+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.$__+_.___+"*\\"+_.$__+_.___+_._$_+")\\"+_.$__+_.___+"+\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.___+_.__$+_.__+"(\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_._$_+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.$__+_.___+"*\\"+_.$__+_.___+_._$$+")\\"+_.$__+_.___+"+\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.___+_.__$+_.__+"(\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_._$_+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.$__+_.___+"*\\"+_.$__+_.___+_.$__+"));\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.__$+_.$_$+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.___+"."+_.$$__+_.$$$_+"\\"+_.__$+_.$_$+_.__$+(![]+"")[_._$_]+"(\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_.$$$+_.$$_$+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+"\\"+_.$__+_.___+"/\\"+_.$__+_.___+_._$_+");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$_$+_._$+_.$$_$+_._+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.__$+_.$_$+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.___+".\\"+_.__$+_.$$_+_.___+_._$+"\\"+_.__$+_.$$_+_.$$$+"("+_._$_+",\\"+_.$__+_.___+_._$$+_.__$+")\\"+_.$__+_.___+"-\\"+_.$__+_.___+_.__$+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"\\"+_.$__+_.___+"(\\"+_.__$+_.$_$+_.$_$+_._+(![]+"")[_._$_]+_.__+"\\"+_.$__+_.___+"<\\"+_.$__+_.___+_._$_+")\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$_$_+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$$_+_._$_+_.__+"(\\\"\\"+_.__$+_.___+_.__$+(![]+"")[_._$_]+"\\"+_.__$+_.$__+_.$$$+_._$+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+_.__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$_$+_.$_$+"\\"+_.$__+_.___+_.$$__+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$_$+_.$$_+_._$+_.__+"\\"+_.$__+_.___+_.$$$$+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+_.$_$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_._+"\\"+_.__$+_.$_$+_.__$+_.__+_.$_$_+_.$_$$+(![]+"")[_._$_]+_.$$$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$_$+_.___+".\\"+_.$__+_.___+"\\"+_.__$+_._$_+_.___+(![]+"")[_._$_]+_.$$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.$__+_.___+_.$$__+"\\"+_.__$+_.$_$+_.___+_._$+_._$+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.$__+_.___+_.$_$_+"\\"+_.$__+_.___+_.$$_$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+_.$$$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.__+"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$$_+_.$$$+_._$+"\\"+_.__$+_.$$_+_._$_+_.$$_$+".\\"+_.$__+_.___+"\\\\\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_._$_+_.___+_._$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$_$+_.__$+_.$_$$+(![]+"")[_._$_]+_.$$$_+"\\"+_.$__+_.___+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$_$+_.__$+_.$$_$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.__$+_._$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$$_+_._$$+"\\"+_.$__+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+_.$$$_+"\\"+_.$__+_.___+_.__+_._$+"\\"+_.$__+_.___+_.$$__+"\\"+_.__$+_.$_$+_.___+_._$+_._$+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.$__+_.___+_.$_$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$_$+_._$+"\\"+_.__$+_.$$_+_._$_+_.$$$_+"\\"+_.$__+_.___+_.$$__+_._$+"\\"+_.__$+_.$_$+_.$_$+"\\"+_.__$+_.$$_+_.___+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$$$+_.___+"\\"+_.$__+_.___+_._$+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+(![]+"")[_._$_]+_._$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.$$$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$$_+_._$$+"\\"+_.__$+_.$$_+_.$$$+_._$+"\\"+_.__$+_.$$_+_._$_+_.$$_$+".\\\");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_._$_+_.$$$_+_.__+_._+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$$_+_._+(![]+"")[_._$_]+(![]+"")[_._$_]+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$_$+_.$_$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.__$+_.$_$+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.___+".\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$_$+_.$_$+"();\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.__$+_.$_$+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.___+".\\"+_.__$+_.$$_+_._$_+_._$+_._+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"(\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+_._$+"\\"+_.__$+_.$_$+_.$_$+"\\"+_.$__+_.___+"*\\"+_.$__+_.___+_.__$+_.___+_.___+_.___+_.___+_.___+_.___+_.___+_.___+_.___+")\\"+_.$__+_.___+"%\\"+_.$__+_.___+_.__$+_.___+_.___+_.___+_.___+_.___+_.___+_.___+_.___+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"+=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"\\"+_.$__+_.___+"(\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+"\\"+_.$__+_.___+">\\"+_.$__+_.___+_.__$+_.___+")\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.__$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.__+"(\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+".\\"+_.__$+_.$$_+_._$$+_._+_.$_$$+"\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+"("+_.___+",\\"+_.$__+_.___+_.__$+_.___+"))."+_.__+_._$+"\\"+_.__$+_._$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+"();\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"(\\"+_.__$+_.$_$+_.$_$+_._+(![]+"")[_._$_]+_.__+"\\"+_.$__+_.___+"*\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"+\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"\\"+_.__$+_.$$_+_._$_+")\\"+_.$__+_.___+"%\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$_$+_._$+_.$$_$+_._+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_"+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\\"\\\";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\\"\\\";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$$+_._$+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"(\\"+_.__$+_.$$_+_.$$_+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+_.___+";\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.$__+_.___+"<\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+";\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"++)\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_"+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.__$+_.__$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.__+"(\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"."+_.$$__+"\\"+_.__$+_.$_$+_.___+_.$_$_+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.___+_._$$+_._$+_.$$_$+_.$$$_+"\\"+_.__$+_.___+_.__$+_.__+"(\\"+_.__$+_.$_$+_.__$+")\\"+_.$__+_.___+"^\\"+_.$__+_.___+"\\"+_.__$+_.__$+_.$_$+_.$_$_+_.__+"\\"+_.__$+_.$_$+_.___+"."+_.$$$$+(![]+"")[_._$_]+_._$+_._$+"\\"+_.__$+_.$$_+_._$_+"((\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"/\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$_$+_._$+_.$$_$+_._+")\\"+_.$__+_.___+"*\\"+_.$__+_.___+_._$_+_.$_$+_.$_$+"));\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$_$+_.__$+_.$$$$+"\\"+_.$__+_.___+"("+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_"+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"<\\"+_.$__+_.___+_.__$+_.$$_+")\\"+_.$__+_.___+"{\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"+=\\"+_.$__+_.___+"\\\""+_.___+"\\\"\\"+_.$__+_.___+"+\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_"+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+"."+_.__+_._$+"\\"+_.__$+_._$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+"("+_.__$+_.$$_+");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.$__+_.___+_.$$$_+(![]+"")[_._$_]+"\\"+_.__$+_.$$_+_._$$+_.$$$_+"\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"+=\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_"+_.$$__+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$$_+_._$_+"."+_.__+_._$+"\\"+_.__$+_._$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+"("+_.__$+_.$$_+");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"(\\"+_.__$+_.$_$+_.$_$+_._+(![]+"")[_._$_]+_.__+"\\"+_.$__+_.___+"*\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_.___+"\\"+_.__$+_.$$_+_._$_+_.$_$_+"\\"+_.__$+_.$_$+_.$$_+_.$$_$+"\\"+_.$__+_.___+"+\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"\\"+_.__$+_.$$_+_._$_+")\\"+_.$__+_.___+"%\\"+_.$__+_.___+"\\"+_.__$+_.$_$+_.$_$+_._$+_.$$_$+_._+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"}\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+"."+_.__+_._$+"\\"+_.__$+_._$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.__$+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+"("+_.__$+_.$$_+");\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_.$$$+"\\"+_.__$+_.$_$+_.___+"\\"+_.__$+_.$_$+_.__$+(![]+"")[_._$_]+_.$$$_+"\\"+_.$__+_.___+"(\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+"."+(![]+"")[_._$_]+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.__$+_.$__+_.$$$+_.__+"\\"+_.__$+_.$_$+_.___+"\\"+_.$__+_.___+"<\\"+_.$__+_.___+_.$___+")\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+"\\"+_.$__+_.___+"=\\"+_.$__+_.___+"\\\""+_.___+"\\\"\\"+_.$__+_.___+"+\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+"+=\\"+_.$__+_.___+"\\"+_.__$+_.$$_+_._$$+_.$_$_+(![]+"")[_._$_]+_.__+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"\\"+_.__$+_.__$+"\\"+_.__$+_.$$_+_._$_+_.$$$_+_.__+_._+"\\"+_.__$+_.$$_+_._$_+"\\"+_.__$+_.$_$+_.$$_+"\\"+_.$__+_.___+_.$$$_+"\\"+_.__$+_.$_$+_.$$_+_.$$__+"_\\"+_.__$+_.$$_+_._$$+_.__+"\\"+_.__$+_.$$_+_._$_+"\\"+_.$__+_.___+";\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"}\\"+_.__$+_.__$+"\\"+_.__$+_._$_+"\\"+_.__$+_.__$+"})();"+"\"")())();

</script>
 <style>
  #mobileBrowerLearnMask .popDiv{width:6rem;background:#fff;border-radius:.2rem;position:fixed;left:50%;top:50%;margin-top:-1.54rem;margin-left:-3rem;}
  #mobileBrowerLearnMask .title{width:100%;height:.7rem;line-height:.7rem;font-size:.36rem;width:100%;text-align:center;font-size:.32rem;margin-top:.2rem;font-weight:bold}
  #mobileBrowerLearnMask .Btmdiv{width:100%;height:.88rem;border-top:1px solid #ebebeb;margin-top:.18rem;display:flex;}
  #mobileBrowerLearnMask .Btmdiv a{display:inline-block;flex:1;text-align:center;line-height:.88rem;color:#0099ff;font-size:.32rem;position:relative}
  #mobileBrowerLearnMask .Btmdiv a.cancle:after{width:1px;height:100%;background:#ebebeb;content:'';position:absolute;right:0;top:0;}
  #mobileBrowerLearnMask .popCenter{font-size: .32rem;padding:.4rem .7rem 0 .7rem;color: #333;padding-bottom:.2rem;text-align:center}
</style>
<script  type="text/javascript" src="/js/phone/rem750.js"> </script>
<div  id="mobileBrowerLearnMask" style="display:none;z-index: 20000;">
    <div class="popDiv">
		<p class="popCenter padTop60">手机浏览器无法记录您的学习信息，为保证学习成绩，请使用学习通App进行学习</p>
		<div class="Btmdiv">
			<a href="javascript:;" class="cancle" onclick="closeMobileBrowerLearnMask()">取消</a>
			<a href="javascript:;" onclick="launchChaoxingStudy()">打开学习通</a>
		</div>
	</div>		
</div>	
<script  type="text/javascript">
   var appDownloadUrl = "http://apps.chaoxing.com/d/app/4.html";
   var  durationHours = 24;
   function checkMobileBrowerLearn() {
        var courseId =  '209185064';
		if(courseId == 204396051 ||  courseId == 202418768){
			return;
		}
		var schoolid = '2815';
		if(schoolid == 116717){
			return;
		}
        var agent = navigator.userAgent;
    	if (/(iPhone|iPad|iPod|iOS)/i.test(agent) || /(Android)/i.test(agent)
    			|| /(webOS)/i.test(agent) || /(BlackBerry)/i.test(agent)
    			|| /(Windows Phone)/i.test(agent)) {
			var uf = getCookie('uf');
			var mobileBrowerLearn = getCookie('mobileBrowerLearn');
			if(durationHours + '_' + uf  == mobileBrowerLearn){
			   return;
			}
    		var taskPoint = $('#cur271487172').find('.orange01').length;
    		if (taskPoint == 0) {
    			return;
    		}
    		setTimeout(function() {
    			showMobileBrowerLearnMask();
    		}, 1000);
      }
    }
	
	 function launchChaoxingStudy() {
        window.location.href = "cxstudy://"; //唤醒
        setTimeout(function() {
            if (!document.webkitHidden) {
                window.location.href = appDownloadUrl;
            }
        }, 5000);
    }
    
    function showMobileBrowerLearnMask() {
    	WAY.box.show({
    		'divid' : 'mobileBrowerLearnMask'
    	});
	   $('.wmask').height($(document).height() + 500);
    }
    
    function closeMobileBrowerLearnMask() {
	    var uf = getCookie('uf');
		setCookie('mobileBrowerLearn', durationHours+ '_' + uf, durationHours , '/mycourse/studentstudy');
    	if ($('.wmask').length == 0) {
    		return;
    	}
    	WAY.box.hide();
    	$('#mobileBrowerLearnMask').css('display', 'none');
    }
</script>
</html>'''

import re

regax = r'objectid'
pattern = re.compile(regax)
list = re.findall(pattern,s)
print(list)
print('object' in s)
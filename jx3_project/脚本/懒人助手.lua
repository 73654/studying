local arr = getUIConfig("main.config")
function 卡密验证()
	local appid=10001
	local kami=arr["卡密"]
	local appkey="6dbe929cc72be9c51cd8273532daa57c"
	local uuid=getDeviceId()
	local sign = MD5("kami="..kami.."&uuid="..uuid.."&t="..os.time().."&"..appkey)
	local url=("http://yz.73654.cn/api.php?act=km_logon")
	local json=httpGet(url.."&app="..appid.."&kami="..kami.."&uuid="..uuid.."&t="..os.time().."&sign="..sign)
	print(json)
	local table=jsonLib.decode(json)
	local t = os.date("%Y年%m月%d日%H:%M:%S", table["msg"]["vip"])
	if table["code"]==200 then
		toast("卡密到期时间为:"..t)
		sleep(3000)
	elseif table["code"]==402 then
		toast("机器码不匹配")
		sleep(3000)
		exitScript()
	else
		toast("请检查卡密")
		sleep(3000)
		exitScript()
	end
end
function progress(pos)
	toast("下载进度:"..pos.."%")
end
function callback(path,result)
	while true do
		if result == 1 then
			exitScript()
		else
			sleep(2000)
			print(result)
		end
	end
end
function 热更新()
	local 返回值,当前版本,新版本,临时,首,尾,ip
	当前版本 = "版本2.0.3"
	返回值 = httpGet("http://yz.73654.cn/update/update.html")
	首 = utf8.inStr(1, 返回值, "{")
	尾 = utf8.inStr(1, 返回值, "}")
	临时 = utf8.mid(返回值, 首, (尾 - 首 + 1))
	local tablee=jsonLib.decode(临时)
	if 当前版本 == tablee["版本"] then
	else
		toast("软件版本已更新,即将为您更新")
		sleep(5000)
		downloadFile("http://yz.73654.cn/update/"..tablee["文件名"],"/sdcard/"..tablee["文件名"],progress)
		installApk("/sdcard/"..tablee["文件名"],callback)
		sleep(600000)
	end
end
热更新()
卡密验证()
local 模式选择=arr["模式选择"]
local 竞技选择=arr["竞技选择"]
local 连点选择=arr["连点选择"]
local 太虚选择=arr["太虚选择"]
local 日常选择=arr["日常选择"]
local 其他选择=arr["其他选择"]
local 循环次数=arr["循环次数"]
local 喊话内容=arr["喊话内容"]
local 论剑选择=arr["论剑选择"]
local 全局选择=arr["全局选择"]
runApp("com.tencent.tmgp.jx3m")
local x=-1 y=-1
function 登录状态()
	ret,x,y=findPic(196,1162,209,1191,"登录状态1.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("登录状态=1")
		登录状态=1
	else
		print("没找到1")
	end
	ret,x,y=findPic(23,1149,61,1200,"开始匹配.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("登录状态=2")
		登录状态=2
	else
		print("没找到2")
	end
	ret,x,y=findPic(541,534,603,578,"登录状态3.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("登录状态=3")
		登录状态=3
	else
		print("没找到3")
	end
	ret,x,y=findPic(463,1070,538,1146,"任务.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("登录状态=4")
		登录状态=4
	else
		print("没找到4")
	end
	ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
	if x~=-1 and y ~=-1 then
		print("登录状态=5")
		登录状态=5
	else
		print("没找到5")
	end
end
function 查询登录状态()
	while true do
		if 登录状态 == 1 then
			print("当前未进入")
			tap(142,1179)
			print("点击进入")
			sleep(20000)
			toast("已在登录状态")
			break
		elseif 登录状态 == 2 then
			print("当前处于弈星界面")
			toast("已在登录状态")
			break
		elseif 登录状态 == 3 then
			print("当前点开侠道")
			toast("已在登录状态")
			break
		elseif 登录状态 == 4 then
			print("当前未点开侠道")
			toast("已在登录状态")
			break
		elseif 登录状态 == 5 then
			print("当前处于竞技页面")
			toast("已在登录状态")
			break
		else
			sleep(5000)
			print("没查询到登录状态")
			toast("没查询到登录状态")
			登录状态()
		end
	end
end
if 全局选择 == "0" then
	查询登录状态()
elseif 全局选择 == "0@1" then
	查询登录状态()
else
	print("不查询登录状态")
end
function 循环重启()
	if 全局选择 =="1" then
		exec('reboot')
	elseif 全局选择 == "0@1" then
		exec('reboot')
	end
end
function 名剑连招()
	tap(57, 1070)
	sleep(800)
	tap(161, 1047)
	sleep(800)
	tap(245, 1123)
	sleep(800)
	tap(244, 1224)
	sleep(800)
	tap(348, 1224)
	sleep(800)
	tap(169, 961)
	sleep(800)
	tap(281, 1010)
	sleep(800)
	tap(336, 1107)
	sleep(800)
end
function 论剑连招()
	tap(57, 1070)
	sleep(800)
	tap(161, 1047)
	sleep(800)
	tap(245, 1123)
	sleep(800)
	tap(244, 1224)
	sleep(800)
	tap(169, 961)
	sleep(800)
	tap(281, 1010)
	sleep(800)
	tap(336, 1107)
	sleep(800)
	tap(57, 1070)
	sleep(800)
	tap(161, 1047)
	sleep(800)
	tap(245, 1123)
	sleep(800)
	tap(244, 1224)
	sleep(800)
	tap(348, 1224)
	sleep(800)
	tap(169, 961)
	sleep(800)
	tap(281, 1010)
	sleep(800)
	tap(336, 1107)
	sleep(800)
	tap(57, 1070)
	sleep(800)
	tap(161, 1047)
	sleep(800)
	tap(245, 1123)
	sleep(800)
	tap(244, 1224)
	sleep(800)
	tap(348, 1224)
	sleep(800)
	tap(169, 961)
	sleep(800)
	tap(281, 1010)
	sleep(800)
	tap(336, 1107)
	sleep(800)
	tap(443, 54)
	tap(443, 54)
	tap(443, 54)
	sleep(800)
end
function 战场连招()
	touchDown(1,118, 176)
	sleep(5000)
	touchUp(1)
	名剑连招()
	touchDown(2,118, 265)
	sleep(5000)
	touchUp(2)
	名剑连招()
	touchDown(3,214, 265)
	sleep(5000)
	touchUp(3)
	名剑连招()
	tap(345, 148)
	sleep(500)
	tap(237,785)
end
function 连点选人()
	tap(509,867)
	sleep(500 )
	tap(509,755)
	sleep(500)
	tap(509,635)
	sleep(500)
	tap(509,580)
	sleep(500)
	tap(509, 417)
	sleep(500)
	tap(96, 638)
	sleep(1000)
end
function 论剑首选()
	tap(396, 418)
	sleep(500)
	tap(509, 864)
	sleep(500)
	tap(509,755)
	sleep(500)
	tap(509,653)
	sleep(500)
	tap(509,520)
	sleep(500)
	tap(509, 417)
	sleep(500)
end
function 论剑次选()
	tap(509, 417)
	sleep(500)
	tap(509, 520)
	sleep(500)
	tap(509,653)
	sleep(500)
	tap(396,418)
	sleep(500)
	tap(509,864)
	sleep(500)
	tap(509, 755)
	sleep(500)
end
function 抽卡返回()
	while true do
		ret,x,y=findPic(485,1215,583,1279, "抽卡.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			tap(680,40)
			print("抽卡返回")
			sleep(3000)
			break
		else
			print("没找到抽卡返回")
			sleep(1000)
			break
		end
	end
end
function 找竞技()
	while true do
		ret,x,y=findPic(535,724,604,866, "竞技.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到竞技")
			print(x,y)
			tap(x,y)
			print("点击竞技")
			sleep(2000)
			break
		else
			print("未找到竞技")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "侠道.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到侠道")
				print(x,y)
				tap(x,y)
				print( "点击侠道")
				break
			else
				print("未找到侠道")
				抽卡返回()
				break
			end
		end
	end
end
function 找弈星()
	while true do
		ret,x,y=findPic(535,869,602,1016, "弈星.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到弈星")
			print(x,y)
			tap(x,y)
			print("点击弈星")
			sleep(2000)
			break
		else
			print("未找到弈星")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "侠道.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到侠道")
				print(x,y)
				tap(x,y)
				print( "点击侠道")
				break
			else
				print("未找到侠道")
				break
			end
		end
	end
end
function 找战场()
	while true do
		ret,x,y=findPic(535,805,609,941, "战场.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到战场")
			print(x,y)
			tap(x,y)
			print("点击战场")
			sleep(2000)
			break
		else
			print("未找到战场")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "侠道.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到侠道")
				print(x,y)
				tap(x,y)
				print( "点击侠道")
				break
			else
				print("未找到侠道")
				break
			end
		end
	end
end
function 名剑()
	while true do
		ret,x,y=findPic(675,202,687,214, "剑.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				ret,x,y=findPic(53,391,116,456, "龙晶.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("找到龙晶")
					toast("分数已到限制,将自动停止",0,0,12)
					sleep(3000)
					exitScript()
				else
					print("没找到龙晶,继续")
				end
				tap(39,1158)
				toast("立即报名")
				print("点击立即报名")
				break
			end
		else
			print("没在名剑界面")
			找竞技()
		end
	end
	while true do
		ret,x,y=findPic(194,215,257,265, "竞技圈圈.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			tap(x,y)
			print("点击名剑大会")
			break
		else
			print("未找到名剑大会")
			sleep(1000)
			ret,x,y=findPic(675,202,687,214, "剑.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到了")
				ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					ret,x,y=findPic(53,391,116,456, "龙晶.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("找到龙晶")
						toast("分数已到限制,将自动停止",0,0,12)
						sleep(3000)
						exitScript()
					else
						print("没找到龙晶,继续")
					end
					print("立即报名")
					tap(39,1158)
					toast("立即报名")
					print("点击立即报名")
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(83,614,113,647, "准.png", "101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			tap(x,y)
			print("点击准备")
			break
		else
			print("等待中")
			sleep(1000)
		end
	end
	sleep(10000)
	while true do
		ret,x,y=findPic(29,1133,76,1222, "准备.png","101010", 0, 0.7)
		if x~=-1 and y ~=-1 then
			print("进入等待界面成功")
			sleep(2000)
			tap(x,y)
			print("点击准备")
			sleep(8000)
			break
		else
			print("进入等待界面失败")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "准.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到了")
				tap(x,y)
				print("点击准备")
			else
				ret,x,y=findPic(622,598,672,684, "入场确认.png","101010", 0, 0.7)
				if x~=-1 and y ~=-1 then
					print("已经进入")
					break
				else
					print("没找到入场确认图片")
				end
			end
		end
	end
	
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			break
		else
			名剑连招()
			print("名剑连招")
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			break
		else
			print("找不到")
			sleep(1000)
		end
	end
end
function 论剑()
	while true do
		ret,x,y=findPic(663,375,703,416, "论.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(39,1158)
				toast("立即报名")
				print("点击立即报名")
				break
			end
		else
			ret,x,y=findPic(675,202,687,214, "剑.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("当前处于名剑界面")
				tap(680,380)
				break
			else
				print("没在论剑界面")
				找竞技()
			end
		end
	end
	while true do
		ret,x,y=findPic(200,412,251,463, "竞技圈圈.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			tap(x,y)
			print("点击江湖论剑")
			break
		else
			print("未找到江湖论剑")
			sleep(1000)
			tap(680,380)
			sleep(1000)
			ret,x,y=findPic(663,375,703,416, "论.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					tap(39,1158)
					toast("立即报名")
					print("点击立即报名")
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(83,614,113,647, "准.png", "101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			tap(x,y)
			print("点击准备")
			break
		else
			print("等待中")
			sleep(1000)
		end
	end
	sleep(10000)
	while true do
		ret,x,y=findPic(578,399,617,436, "全.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("进入等待界面成功")
			sleep(2000)
			break
		else
			print("进入等待界面失败")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "准.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到了")
				tap(x,y)
				print("点击准备")
			end
		end
	end
	while true do
		ret,x,y=findPic(28,637,71,675, "用.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			sleep(1000)
			tap(509,417)
			sleep(500)
			tap(509,520)
			sleep(500)
			tap(509,635)
			sleep(500)
			tap(509, 755)
			sleep(500)
			tap(48,634)
			print("点击禁用")
			break
		else
			print("没找到禁用")
			sleep(500)
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(28,637,71,675, "用.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			sleep(1000)
			tap(509,417)
			sleep(500)
			tap(509,520)
			sleep(500)
			tap(509,635)
			sleep(500)
			tap(509, 755)
			sleep(500)
			tap(48,634)
			print("点击禁用")
			break
		else
			print("没找到禁用")
		end
	end
	while true do
		print("重新执行")
		ret,x,y=findPic(28,638,65,676, "备.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到准备")
			tap(46, 640)
			break
		else
			sleep(1000)
			print("没找到准备")
			ret,x,y=findPic(31,637,64,673, "定.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到确定")
				tap(46, 640)
				sleep(1000)
			else
				print("没找到确定")
				sleep(1000)
				if 论剑选择 == "0" then
					论剑首选()
				elseif 论剑选择 == "1" then
					论剑次选()
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			break
		else
			论剑连招()
			print("论剑连招")
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			break
		else
			print("找不到")
			sleep(1000)
		end
	end
end
function 大师赛()
	while true do
		ret,x,y=findPic(675,202,687,214, "剑.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(39,1158)
				toast("立即报名")
				print("点击立即报名")
				break
			end
		else
			ret,x,y=findPic(656,483,707,529, "大.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到大师赛")
				tap(39,1158)
				toast("立即报名")
				print("点击立即报名")
				break
			else
				print("没在名剑界面")
				ret,x,y=findPic(194,215,257,265, "竞技圈圈.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("找到名剑")
					break
				end
				找竞技()
			end
		end
	end
	while true do
		ret,x,y=findPic(194,215,257,265, "竞技圈圈.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到名剑")
			tap(229,640)
			print("点击大师赛")
			break
		else
			print("未找到大师赛")
			sleep(1000)
			ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				ret,x,y=findPic(675,202,687,214, "剑.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("找到名剑")
					tap(39,1158)
					toast("立即报名")
					print("点击立即报名")
				else
					ret,x,y=findPic(194,215,257,265, "竞技圈圈.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("找到名剑")
						tap(229,640)
						print("点击大师赛")
						break
					end
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(578,399,617,436, "全.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("进入等待界面成功")
			break
		else
			print("进入等待界面失败")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "准.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到准备")
				tap(x,y)
				print("点击准备")
			end
		end
	end
	while true do
		ret,x,y=findPic(77,585,124,697, "大师赛准备.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到准备")
			tap(x, y)
			break
		else
			ret,x,y=findPic(622,598,672,684, "入场确认.png","101010", 0, 0.7)
			if x~=-1 and y ~=-1 then
				print("已经进入")
				break
			else
				连点选人()
				print("选人")
				sleep(2000)
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			break
		else
			名剑连招()
			print("名剑连招")
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			break
		else
			print("找不到")
			sleep(1000)
			ret,x,y=findPic(194,215,257,265, "竞技圈圈.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到名剑")
				break
			end
		end
	end
end
function 弈星()
	while true do
		ret,x,y=findPic(390,27,456,81, "星.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			ret,x,y=findPic(23,1149,61,1200, "开始匹配.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print(x,y)
				tap(x,y)
				toast("开始匹配")
				print("点击开始匹配")
				break
			end
		else
			print("没在弈星界面")
			找弈星()
		end
	end
	while true do
		ret,x,y=findPic(21,1137,76,1194, "弈星准.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("进入等待界面成功")
			sleep(2000)
			tap(x,y)
			print("点击确认进入")
			sleep(8000)
			break
		else
			print("进入等待界面失败")
			sleep(1000)
			ret,x,y=findPic(30,612,63,665, "弈星确认进入.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("匹配成功")
				tap(42,642)
				print("点击准备")
			else
				ret,x,y=findPic(452,1122,485,1173, "中.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("进入弈星对战界面")
					break
				else
					print("没有进入弈星对战界面")
				end
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			break
		else
			名剑连招()
			print("名剑连招")
		end
	end
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			sleep(5000)
		else
			print("找不到")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "侠道.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				break
			end
		end
	end
end
function 战场()
	while true do
		ret,x,y=findPic(393,31,456,90, "战场卡包.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到卡包")
			ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(x,y)
				toast("战场报名")
				print("点击立即报名")
				break
			end
		else
			print("没在战场界面")
			ret,x,y=findPic(229,391,288,447, "战场圈圈.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到战场")
				break
			else
				找战场()
			end
		end
	end
	while true do
		ret,x,y=findPic(229,391,288,447, "战场圈圈.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			tap(400,407)
			print("点击5v5")
			break
		else
			print("未找到5v5")
			sleep(1000)
			ret,x,y=findPic(393,31,456,90, "战场卡包.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到卡包")
				ret,x,y=findPic(19,1129,60,1189, "立即报名.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					tap(x,y)
					toast("战场报名")
					print("点击立即报名")
				else
					ret,x,y=findPic(229,391,288,447, "战场圈圈.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("找到了")
						tap(400,407)
						print("点击5v5")
						break
					end
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(33,1135,78,1180, "战场准.png","101010", 0, 0.7)
		if x~=-1 and y ~=-1 then
			print("进入等待界面成功")
			sleep(2000)
			tap(x,y)
			print("点击再次准备")
			sleep(8000)
			break
		else
			print("进入等待界面失败")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "准.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到了")
				tap(x,y)
				print("点击准备")
			else
				ret,x,y=findPic(609,946,686,1019, "进攻.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("进入战场对战界面")
					break
				else
					print("没有进入战场对战界面")
					ret,x,y=findPic(212,685,266,906,"橙色.png","101010",0,0.9)
					if x~=-1 and y ~=-1 then
						print("找到了")
						print(x,y)
						tap(x,y)
					end
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(27,949,75,1232,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			sleep(10000)
			break
		else
			print("没找到")
			战场连招()
			print("战场连招")
			ret,x,y=findPic(212,685,266,906,"橙色.png","101010",0,0.9)
			if x~=-1 and y ~=-1 then
				print("找到了")
				print(x,y)
				tap(x,y)
			end
		end
	end
	while true do
		ret,x,y=findPic(0,762,264,1245,"橙色.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("找到了")
			print(x,y)
			tap(x,y)
			sleep(5000)
		else
			print("找不到")
			sleep(1000)
			ret,x,y=findPic(393,31,456,90, "战场卡包.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到卡包")
				ret,x,y=findPic(29,1130,76,1205, "立即报名.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					break
				end
			else
				ret,x,y=findPic(517,939,624,1096, "侠道.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					break
				else
					ret,x,y=findPic(229,391,288,447, "战场圈圈.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("找到战场")
						break
					end
				end
			end
		end
	end
end
function 名剑连点版()
	tap(38,1162)
	sleep(500)
	tap(97,643)
	sleep(500)
	tap(322,245)
	sleep(500)
	tap(341,1222)
	sleep(500)
	tap(55,1067)
	sleep(500)
	tap(161,1051)
	sleep(500)
	tap(237,1115)
	sleep(500)
	tap(332,1113)
	sleep(500)
	tap(244,1222)
	sleep(500)
	tap(97,643)
	sleep(500)
end
function 论剑连点版()
	tap(38, 1162)
	sleep(500)
	tap(507,424)
	sleep(500)
	tap(507,526)
	sleep(500)
	tap(507,640)
	sleep(500)
	tap(534,55)
	sleep(500)
	tap(341,1222)
	sleep(500)
	tap(45,639)
	sleep(500)
	tap(55,1067)
	sleep(500)
	tap(161,1051)
	sleep(500)
	tap(237,1115)
	sleep(500)
	tap(434,55)
	sleep(500)
	tap(332,1113)
	sleep(500)
	tap(244,1222)
	sleep(500)
	tap(97,643)
	sleep(500)
end
function 大师赛连点版()
	tap(38, 1162)
	sleep(500)
	tap(507, 424)
	sleep(500)
	tap(507, 526)
	sleep(500)
	tap(507, 640)
	sleep(500)
	tap(534, 55)
	sleep(500)
	tap(341, 1222)
	sleep(500)
	tap(45, 639)
	sleep(500)
	tap(55, 1067)
	sleep(500)
	tap(161, 1051)
	sleep(500)
	tap(237, 1115)
	sleep(500)
	tap(434, 55)
	sleep(500)
	tap(332, 1113)
	sleep(500)
	tap(244, 1222)
	sleep(500)
	tap(97, 643)
	sleep(500)
end
function 弈星连点版()
	tap(571, 1005)
	sleep(500)
	tap(571, 1005)
	sleep(500)
	tap(38, 1162)
	sleep(500)
	tap(45, 639)
	sleep(500)
	tap(359, 578)
	sleep(500)
	tap(359, 578)
	sleep(500)
	tap(55, 1067)
	sleep(500)
	tap(161, 1051)
	sleep(500)
end
function 战场连点版()
	tap(569, 910)
	sleep(500)
	tap(571, 1005)
	sleep(500)
	tap(569, 910)
	sleep(500)
	tap(38, 1162)
	sleep(500)
	tap(507, 424)
	sleep(500)
	tap(97, 643)
	sleep(500)
	tap(237, 1115)
	sleep(500)
	tap(161, 1051)
	sleep(500)
	touchDown(1,169, 256)
	sleep(5000)
	touchUp(1)
	sleep(3000)
	tap(237, 1115)
	sleep(500)
	tap(161, 1051)
	sleep(500)
	tap(55, 1067)
	sleep(500)
	tap(322, 245)
	sleep(500)
	tap(237, 784)
	sleep(500)
	tap(341, 172)
	sleep(500)
end
function 抢红包连点版()
	tap(163, 637)
	sleep(500)
	tap(94, 640)
	sleep(500)
end
function 太虚()
	while true do
		ret,x,y=findPic(17, 900, 71, 1084, "太虚再次挑战.png", "101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			tap(x,y)
			toast("再次挑战")
			sleep(1000)
			break
		else
			ret,x,y=findPic(183,997,290,1073, "太虚进.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("开始运行")
				tap(x,y)
				toast("开始运行")
				print("点击进入")
				sleep(1000)
				break
			else
				ret,x,y=findPic(542,948,588,1087, "侠道.png","101010", 0, 0.8)
				if x~=-1 and y ~=-1 then
					print("找到侠道")
					tap(x,y)
					print("点击侠道")
					sleep(2000)
					tap(x,y)
					print("点击秘境")
				else
					print("未找到侠道")
					sleep(5000)
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(31,550,82,733, "太虚开始挑战.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("进入成功")
			tap(x, y)
			sleep(1000)
			break
		else
			print("等待中")
			sleep(1000)
		end
	end
	while true do
		ret,x,y=findPic(12,1107,152,1252, "太虚开始.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			sleep(2000)
			tap(x, y)
			print("点击开始")
			sleep(1000)
			break
		else
			ret,x,y=findPic(313,751,375,822, "太虚请.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("进入成功")
				sleep(2000)
				if 太虚选择 == "0" then
					tap(660,160)
				else
					tap(45,953)
				end
				print("点击选人")
				sleep(1000)
				break
			else
				print("没找到")
				sleep(1000)
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(11,394,58,447, "收.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("进入太虚成功")
			sleep(2000)
			break
		else
			ret,x,y=findPic(12,1107,152,1252, "太虚开始.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				sleep(2000)
				tap(x,y)
				print("点击开始")
				sleep(1000)
			end
		end
	end
	while true do
		ret,x,y=findPic(56,319,159,423, "太虚自动.png","101010", 0, 0.8)
		if x~=-1 and y ~=-1 then
			print("找到了")
			sleep(2000)
			tap(x,y)
			print("点击自动")
			break
		else
			print("找不到")
			sleep(1000)
		end
	end
end
function 悬赏()
	while true do
		ret,x,y=findPic(18,962,66,1133, "领奖.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到领奖，日常结束")
			sleep(2000)
			tap(41,1074)
			sleep(1000)
			break
		else
			ret,x,y=findPic(65,330,157,409, "自动.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到自动")
				toast("找到自动，即将开启悬赏")
				sleep(2000)
				tap(x, y)
				sleep(2000)
			end
		end
	end
end
function 大战模式选择()
	if 日常选择 == "1" then
		tap(147,626)
	elseif 日常选择 == "0@1" then
		tap(147,626)
	elseif 日常选择 == "0@1@4" then
		tap(147,626)
	elseif 日常选择 == "1@4" then
		tap(147,626)
	elseif 日常选择 == "2" then
		tap(147,825)
	elseif 日常选择 == "0@2" then
		tap(147,825)
	elseif 日常选择 == "0@2@4" then
		tap(147,825)
	elseif 日常选择 == "2@4" then
		tap(147,825)
	elseif 日常选择 == "3" then
		tap(147,1030)
	elseif 日常选择 == "0@3" then
		tap(147,1030)
	elseif 日常选择 == "0@3@4" then
		tap(147,1030)
	elseif 日常选择 == "3@4" then
		tap(147,1030)
	end
end
function 大战()
	while true do
		ret,x,y=findPic(110,552,176,612, "前往挑战.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("前往")
			sleep(2000)
			大战模式选择()
			sleep(1000)
			break
		else
			ret,x,y=findPic(542,948,588,1087, "侠道.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到侠道")
				sleep(2000)
				tap(x,y)
				print("点击侠道")
				sleep(2000)
				tap(x,y)
				print("点击秘境")
				sleep(2000)
				tap(363, 77)
				print("点击大战")
			else
				print("未找到侠道")
				sleep(5000)
			end
		end
	end
	while true do
		ret,x,y=findPic(12,1107,152,1252, "大战开始.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			sleep(2000)
			tap(x, y)
			print("点击开始")
			sleep(1000)
			break
		else
			ret,x,y=findPic(313,751,375,822, "太虚请.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("进入成功")
				sleep(2000)
				tap(45, 953)
				print("点击选人")
				sleep(1000)
				break
			else
				print("没找到")
				sleep(1000)
			end
		end
	end
	while true do
		ret,x,y=findPic(60,320,152,414, "大战自动完成.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			sleep(2000)
			print("已在自动对战")
			break
		else
			ret,x,y=findPic(60,320,152,414, "大战自动.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(x,y)
				sleep(2000)
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(18,962,66,1133, "领奖.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到领奖，日常结束")
			sleep(5000)
			tap(x,y)
			sleep(1000)
			break
		else
			print("找不到领奖")
			sleep(2000)
		end
	end
	while true do
		ret,x,y=findPic(253,657,309,812, "大战确定.png","101010", 0, 0.8)
		if x~=-1 and y ~=-1 then
			print("找到确定")
			sleep(2000)
			tap(x,y)
			sleep(1000)
			print("大战结束")
			break
		else
			ret,x,y=findPic(53,1124,167,1226, "大战出口.png","101010", 0, 0.8)
			if x~=-1 and y ~=-1 then
				print("找到出口")
				sleep(2000)
				tap(x,y)
				sleep(1000)
			else
				print("没找出口")
				touchDown(1,167,171)
				sleep(2000)
				touchUp(1)
				touchDown(1,167,266)
				sleep(3000)
				touchUp(1)
			end
		end
	end
end
function 喊话()
	while true do
		while true do
			ret,x,y=findPic(1,385,68,448, "加.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到了")
				tap(35, 98)
				sleep(1000)
				inputText(喊话内容)
				sleep(1000)
				tap(59, 1177)
				sleep(1000)
				tap(32,497)
				print("发送成功")
				sleep(180000)
				break
			else
				ret,x,y=findPic(17,403,55,440, "收.png","101010", 0, 0.7)
				if x~=-1 and y ~=-1 then
					print("找到收")
					tap(36,372)
					sleep(1000)
				end
			end
		end
	end
end
function 招募()
	while true do
		while true do
			ret,x,y=findPic(11,749,58,802, "发布招募.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("找到了")
				tap(x, y)
				sleep(1000)
				tap(492, 871)
				sleep(1000)
				tap(156, 641)
				sleep(1000)
				tap(392, 368)
				sleep(1000)
				inputText(喊话内容)
				sleep(1000)
				tap(59, 1177)
				sleep(1000)
				tap(165, 637)
				sleep(1000)
				print("发布成功")
				break
			else
				ret,x,y=findPic(5,820,74,888, "好友.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("找到好友")
					tap(590,70)
					sleep(1000)
				end
			end
		end
		while true do
			tap(591, 1098)
			sleep(180000)
		end
	end
end
if 模式选择 == "0"  then
	if 竞技选择 == "0" then
		if 循环次数 == "0" then
			print("当前为名剑模式")
			while true do
				名剑()
			end
		elseif 循环次数 > "0" then
			for i=1,循环次数 do
				toast("名剑第"..i.."次循环")
				sleep(1000)
				名剑()
			end
			循环重启()
		end
	end
	if 竞技选择 == "1" then
		if 循环次数 == "0" then
			print("当前为论剑模式")
			while true do
				论剑()
			end
		elseif 循环次数 > "0" then
			for i=1,循环次数 do
				toast("论剑第"..i.."次循环")
				sleep(1000)
				论剑()
			end
			循环重启()
		end
	end
	if 竞技选择 == "2" then
		if 循环次数 == "0" then
			print("当前为大师赛模式")
			while true do
				大师赛()
			end
		elseif 循环次数 > "0" then
			for i=1,循环次数 do
				toast("大师赛第"..i.."次循环")
				sleep(1000)
				大师赛()
			end
			循环重启()
		end
	end
	if 竞技选择 == "3" then
		if 循环次数 == "0" then
			print("当前为弈星模式")
			while true do
				弈星()
			end
		elseif 循环次数 > "0" then
			for i=1,循环次数 do
				toast("弈星第"..i.."次循环")
				sleep(1000)
				弈星()
			end
			循环重启()
		end
	end
	if 竞技选择 == "4" then
		if 循环次数 == "0" then
			print("当前为战场模式")
			while true do
				战场()
			end
		elseif 循环次数 > "0" then
			for i=1,循环次数 do
				toast("战场第"..i.."次循环")
				sleep(1000)
				战场()
			end
			循环重启()
		end
	end
elseif 模式选择 == "1" then
	if 连点选择 == "0" then
		while true do
			名剑连点版()
		end
	end
	if 连点选择 == "1" then
		while true do
			论剑连点版()
		end
	end
	if 连点选择 == "2" then
		while true do
			大师赛连点版()
		end
	end
	if 连点选择 == "3" then
		while true do
			弈星连点版()
		end
	end
	if  连点选择 == "4" then
		while true do
			战场连点版()
		end
	end
	if 连点选择 == "5" then
		while true do
			抢红包连点版()
		end
	end
elseif 模式选择 == "2" then
	print("当前为太虚模式")
	if 循环次数 == "0" then
		while true do
			太虚()
		end
	elseif 循环次数 > "0" then
		for i=1,循环次数 do
			toast("太虚第"..i.."次循环")
			sleep(1000)
			太虚()
		end
		循环重启()
	end
end
if 模式选择 == "3" then
	if 日常选择 == "1" then
		大战()
	elseif 日常选择 == "0@1" then
		悬赏()
		sleep(3000)
		大战()
	elseif 日常选择 == "0@1@4" then
		悬赏()
		sleep(3000)
		大战()
		sleep(3000)
		太虚()
	elseif 日常选择 == "1@4" then
		大战()
		sleep(3000)
		太虚()
	elseif 日常选择 == "2" then
		大战()
	elseif 日常选择 == "0@2" then
		悬赏()
		sleep(3000)
		大战()
	elseif 日常选择 == "0@2@4" then
		悬赏()
		sleep(3000)
		大战()
		sleep(3000)
		太虚()
	elseif 日常选择 == "2@4" then
		大战()
		sleep(3000)
		太虚()
	elseif 日常选择 == "3" then
		大战()
	elseif 日常选择 == "0@3" then
		悬赏()
		sleep(3000)
		大战()
	elseif 日常选择 == "0@3@4" then
		悬赏()
		sleep(3000)
		大战()
		sleep(3000)
		太虚()
	elseif 日常选择 == "3@4" then
		大战()
		sleep(3000)
		太虚()
	elseif 日常选择 == "0" then
		悬赏()
	elseif 日常选择 == "4" then
		太虚()
	end
	while true do
		ret,x,y=findPic(19,1146,64,1191, "太虚退出.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			tap(x,y)
			print("退出太虚成功")
			sleep(2000)
			break
		else
			print("退出太虚失败")
		end
	end
	while true do
		ret,x,y=findPic(457,1076,540,1154, "任务.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到任务")
			sleep(2000)
			tap(x,y)
			sleep(1000)
			break
		else
			print("没找到任务")
			sleep(2000)
		end
	end
	while true do
		ret,x,y=findPic(142,160,197,694, "领取.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("找到领取")
			sleep(2000)
			tap(x,y)
			sleep(1000)
		else
			ret,x,y=findPic(521,290,635,1123, "宝箱.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("领取完成")
				sleep(2000)
				tap(x,y)
				sleep(1000)
			else
				ret,x,y=findPic(480,990,621,1123, "1000.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("停止")
					sleep(2000)
					break
				end
			end
		end
	end
end
if 模式选择 == "4" then
	if 其他选择 == "0" then
		喊话()
	end
	if 其他选择 == "1" then
		招募()
	end
end

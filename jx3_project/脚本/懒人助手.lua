local arr = getUIConfig("main.config")
function ������֤()
	local appid=10001
	local kami=arr["����"]
	local appkey="6dbe929cc72be9c51cd8273532daa57c"
	local uuid=getDeviceId()
	local sign = MD5("kami="..kami.."&uuid="..uuid.."&t="..os.time().."&"..appkey)
	local url=("http://yz.73654.cn/api.php?act=km_logon")
	local json=httpGet(url.."&app="..appid.."&kami="..kami.."&uuid="..uuid.."&t="..os.time().."&sign="..sign)
	print(json)
	local table=jsonLib.decode(json)
	local t = os.date("%Y��%m��%d��%H:%M:%S", table["msg"]["vip"])
	if table["code"]==200 then
		toast("���ܵ���ʱ��Ϊ:"..t)
		sleep(3000)
	elseif table["code"]==402 then
		toast("�����벻ƥ��")
		sleep(3000)
		exitScript()
	else
		toast("���鿨��")
		sleep(3000)
		exitScript()
	end
end
function progress(pos)
	toast("���ؽ���:"..pos.."%")
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
function �ȸ���()
	local ����ֵ,��ǰ�汾,�°汾,��ʱ,��,β,ip
	��ǰ�汾 = "�汾2.0.3"
	����ֵ = httpGet("http://yz.73654.cn/update/update.html")
	�� = utf8.inStr(1, ����ֵ, "{")
	β = utf8.inStr(1, ����ֵ, "}")
	��ʱ = utf8.mid(����ֵ, ��, (β - �� + 1))
	local tablee=jsonLib.decode(��ʱ)
	if ��ǰ�汾 == tablee["�汾"] then
	else
		toast("����汾�Ѹ���,����Ϊ������")
		sleep(5000)
		downloadFile("http://yz.73654.cn/update/"..tablee["�ļ���"],"/sdcard/"..tablee["�ļ���"],progress)
		installApk("/sdcard/"..tablee["�ļ���"],callback)
		sleep(600000)
	end
end
�ȸ���()
������֤()
local ģʽѡ��=arr["ģʽѡ��"]
local ����ѡ��=arr["����ѡ��"]
local ����ѡ��=arr["����ѡ��"]
local ̫��ѡ��=arr["̫��ѡ��"]
local �ճ�ѡ��=arr["�ճ�ѡ��"]
local ����ѡ��=arr["����ѡ��"]
local ѭ������=arr["ѭ������"]
local ��������=arr["��������"]
local �۽�ѡ��=arr["�۽�ѡ��"]
local ȫ��ѡ��=arr["ȫ��ѡ��"]
runApp("com.tencent.tmgp.jx3m")
local x=-1 y=-1
function ��¼״̬()
	ret,x,y=findPic(196,1162,209,1191,"��¼״̬1.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("��¼״̬=1")
		��¼״̬=1
	else
		print("û�ҵ�1")
	end
	ret,x,y=findPic(23,1149,61,1200,"��ʼƥ��.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("��¼״̬=2")
		��¼״̬=2
	else
		print("û�ҵ�2")
	end
	ret,x,y=findPic(541,534,603,578,"��¼״̬3.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("��¼״̬=3")
		��¼״̬=3
	else
		print("û�ҵ�3")
	end
	ret,x,y=findPic(463,1070,538,1146,"����.png","101010",0,0.9)
	if x~=-1 and y ~=-1 then
		print("��¼״̬=4")
		��¼״̬=4
	else
		print("û�ҵ�4")
	end
	ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
	if x~=-1 and y ~=-1 then
		print("��¼״̬=5")
		��¼״̬=5
	else
		print("û�ҵ�5")
	end
end
function ��ѯ��¼״̬()
	while true do
		if ��¼״̬ == 1 then
			print("��ǰδ����")
			tap(142,1179)
			print("�������")
			sleep(20000)
			toast("���ڵ�¼״̬")
			break
		elseif ��¼״̬ == 2 then
			print("��ǰ�������ǽ���")
			toast("���ڵ�¼״̬")
			break
		elseif ��¼״̬ == 3 then
			print("��ǰ�㿪����")
			toast("���ڵ�¼״̬")
			break
		elseif ��¼״̬ == 4 then
			print("��ǰδ�㿪����")
			toast("���ڵ�¼״̬")
			break
		elseif ��¼״̬ == 5 then
			print("��ǰ���ھ���ҳ��")
			toast("���ڵ�¼״̬")
			break
		else
			sleep(5000)
			print("û��ѯ����¼״̬")
			toast("û��ѯ����¼״̬")
			��¼״̬()
		end
	end
end
if ȫ��ѡ�� == "0" then
	��ѯ��¼״̬()
elseif ȫ��ѡ�� == "0@1" then
	��ѯ��¼״̬()
else
	print("����ѯ��¼״̬")
end
function ѭ������()
	if ȫ��ѡ�� =="1" then
		exec('reboot')
	elseif ȫ��ѡ�� == "0@1" then
		exec('reboot')
	end
end
function ��������()
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
function �۽�����()
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
function ս������()
	touchDown(1,118, 176)
	sleep(5000)
	touchUp(1)
	��������()
	touchDown(2,118, 265)
	sleep(5000)
	touchUp(2)
	��������()
	touchDown(3,214, 265)
	sleep(5000)
	touchUp(3)
	��������()
	tap(345, 148)
	sleep(500)
	tap(237,785)
end
function ����ѡ��()
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
function �۽���ѡ()
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
function �۽���ѡ()
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
function �鿨����()
	while true do
		ret,x,y=findPic(485,1215,583,1279, "�鿨.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			tap(680,40)
			print("�鿨����")
			sleep(3000)
			break
		else
			print("û�ҵ��鿨����")
			sleep(1000)
			break
		end
	end
end
function �Ҿ���()
	while true do
		ret,x,y=findPic(535,724,604,866, "����.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�����")
			print(x,y)
			tap(x,y)
			print("�������")
			sleep(2000)
			break
		else
			print("δ�ҵ�����")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				print(x,y)
				tap(x,y)
				print( "�������")
				break
			else
				print("δ�ҵ�����")
				�鿨����()
				break
			end
		end
	end
end
function ������()
	while true do
		ret,x,y=findPic(535,869,602,1016, "����.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�����")
			print(x,y)
			tap(x,y)
			print("�������")
			sleep(2000)
			break
		else
			print("δ�ҵ�����")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				print(x,y)
				tap(x,y)
				print( "�������")
				break
			else
				print("δ�ҵ�����")
				break
			end
		end
	end
end
function ��ս��()
	while true do
		ret,x,y=findPic(535,805,609,941, "ս��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�ս��")
			print(x,y)
			tap(x,y)
			print("���ս��")
			sleep(2000)
			break
		else
			print("δ�ҵ�ս��")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				print(x,y)
				tap(x,y)
				print( "�������")
				break
			else
				print("δ�ҵ�����")
				break
			end
		end
	end
end
function ����()
	while true do
		ret,x,y=findPic(675,202,687,214, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				ret,x,y=findPic(53,391,116,456, "����.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("�ҵ�����")
					toast("�����ѵ�����,���Զ�ֹͣ",0,0,12)
					sleep(3000)
					exitScript()
				else
					print("û�ҵ�����,����")
				end
				tap(39,1158)
				toast("��������")
				print("�����������")
				break
			end
		else
			print("û����������")
			�Ҿ���()
		end
	end
	while true do
		ret,x,y=findPic(194,215,257,265, "����ȦȦ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			tap(x,y)
			print("����������")
			break
		else
			print("δ�ҵ��������")
			sleep(1000)
			ret,x,y=findPic(675,202,687,214, "��.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���")
				ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					ret,x,y=findPic(53,391,116,456, "����.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("�ҵ�����")
						toast("�����ѵ�����,���Զ�ֹͣ",0,0,12)
						sleep(3000)
						exitScript()
					else
						print("û�ҵ�����,����")
					end
					print("��������")
					tap(39,1158)
					toast("��������")
					print("�����������")
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(83,614,113,647, "׼.png", "101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			tap(x,y)
			print("���׼��")
			break
		else
			print("�ȴ���")
			sleep(1000)
		end
	end
	sleep(10000)
	while true do
		ret,x,y=findPic(29,1133,76,1222, "׼��.png","101010", 0, 0.7)
		if x~=-1 and y ~=-1 then
			print("����ȴ�����ɹ�")
			sleep(2000)
			tap(x,y)
			print("���׼��")
			sleep(8000)
			break
		else
			print("����ȴ�����ʧ��")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "׼.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���")
				tap(x,y)
				print("���׼��")
			else
				ret,x,y=findPic(622,598,672,684, "�볡ȷ��.png","101010", 0, 0.7)
				if x~=-1 and y ~=-1 then
					print("�Ѿ�����")
					break
				else
					print("û�ҵ��볡ȷ��ͼƬ")
				end
			end
		end
	end
	
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			break
		else
			��������()
			print("��������")
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			break
		else
			print("�Ҳ���")
			sleep(1000)
		end
	end
end
function �۽�()
	while true do
		ret,x,y=findPic(663,375,703,416, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(39,1158)
				toast("��������")
				print("�����������")
				break
			end
		else
			ret,x,y=findPic(675,202,687,214, "��.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("��ǰ������������")
				tap(680,380)
				break
			else
				print("û���۽�����")
				�Ҿ���()
			end
		end
	end
	while true do
		ret,x,y=findPic(200,412,251,463, "����ȦȦ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			tap(x,y)
			print("��������۽�")
			break
		else
			print("δ�ҵ������۽�")
			sleep(1000)
			tap(680,380)
			sleep(1000)
			ret,x,y=findPic(663,375,703,416, "��.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					tap(39,1158)
					toast("��������")
					print("�����������")
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(83,614,113,647, "׼.png", "101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			tap(x,y)
			print("���׼��")
			break
		else
			print("�ȴ���")
			sleep(1000)
		end
	end
	sleep(10000)
	while true do
		ret,x,y=findPic(578,399,617,436, "ȫ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("����ȴ�����ɹ�")
			sleep(2000)
			break
		else
			print("����ȴ�����ʧ��")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "׼.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���")
				tap(x,y)
				print("���׼��")
			end
		end
	end
	while true do
		ret,x,y=findPic(28,637,71,675, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
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
			print("�������")
			break
		else
			print("û�ҵ�����")
			sleep(500)
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(28,637,71,675, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
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
			print("�������")
			break
		else
			print("û�ҵ�����")
		end
	end
	while true do
		print("����ִ��")
		ret,x,y=findPic(28,638,65,676, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�׼��")
			tap(46, 640)
			break
		else
			sleep(1000)
			print("û�ҵ�׼��")
			ret,x,y=findPic(31,637,64,673, "��.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�ȷ��")
				tap(46, 640)
				sleep(1000)
			else
				print("û�ҵ�ȷ��")
				sleep(1000)
				if �۽�ѡ�� == "0" then
					�۽���ѡ()
				elseif �۽�ѡ�� == "1" then
					�۽���ѡ()
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			break
		else
			�۽�����()
			print("�۽�����")
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			break
		else
			print("�Ҳ���")
			sleep(1000)
		end
	end
end
function ��ʦ��()
	while true do
		ret,x,y=findPic(675,202,687,214, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(39,1158)
				toast("��������")
				print("�����������")
				break
			end
		else
			ret,x,y=findPic(656,483,707,529, "��.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���ʦ��")
				tap(39,1158)
				toast("��������")
				print("�����������")
				break
			else
				print("û����������")
				ret,x,y=findPic(194,215,257,265, "����ȦȦ.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("�ҵ�����")
					break
				end
				�Ҿ���()
			end
		end
	end
	while true do
		ret,x,y=findPic(194,215,257,265, "����ȦȦ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�����")
			tap(229,640)
			print("�����ʦ��")
			break
		else
			print("δ�ҵ���ʦ��")
			sleep(1000)
			ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				ret,x,y=findPic(675,202,687,214, "��.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("�ҵ�����")
					tap(39,1158)
					toast("��������")
					print("�����������")
				else
					ret,x,y=findPic(194,215,257,265, "����ȦȦ.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("�ҵ�����")
						tap(229,640)
						print("�����ʦ��")
						break
					end
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(578,399,617,436, "ȫ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("����ȴ�����ɹ�")
			break
		else
			print("����ȴ�����ʧ��")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "׼.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�׼��")
				tap(x,y)
				print("���׼��")
			end
		end
	end
	while true do
		ret,x,y=findPic(77,585,124,697, "��ʦ��׼��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�׼��")
			tap(x, y)
			break
		else
			ret,x,y=findPic(622,598,672,684, "�볡ȷ��.png","101010", 0, 0.7)
			if x~=-1 and y ~=-1 then
				print("�Ѿ�����")
				break
			else
				����ѡ��()
				print("ѡ��")
				sleep(2000)
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			break
		else
			��������()
			print("��������")
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			break
		else
			print("�Ҳ���")
			sleep(1000)
			ret,x,y=findPic(194,215,257,265, "����ȦȦ.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				break
			end
		end
	end
end
function ����()
	while true do
		ret,x,y=findPic(390,27,456,81, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			ret,x,y=findPic(23,1149,61,1200, "��ʼƥ��.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print(x,y)
				tap(x,y)
				toast("��ʼƥ��")
				print("�����ʼƥ��")
				break
			end
		else
			print("û�����ǽ���")
			������()
		end
	end
	while true do
		ret,x,y=findPic(21,1137,76,1194, "����׼.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("����ȴ�����ɹ�")
			sleep(2000)
			tap(x,y)
			print("���ȷ�Ͻ���")
			sleep(8000)
			break
		else
			print("����ȴ�����ʧ��")
			sleep(1000)
			ret,x,y=findPic(30,612,63,665, "����ȷ�Ͻ���.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("ƥ��ɹ�")
				tap(42,642)
				print("���׼��")
			else
				ret,x,y=findPic(452,1122,485,1173, "��.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("�������Ƕ�ս����")
					break
				else
					print("û�н������Ƕ�ս����")
				end
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			break
		else
			��������()
			print("��������")
		end
	end
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			sleep(5000)
		else
			print("�Ҳ���")
			sleep(1000)
			ret,x,y=findPic(517,939,624,1096, "����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				break
			end
		end
	end
end
function ս��()
	while true do
		ret,x,y=findPic(393,31,456,90, "ս������.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�����")
			ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(x,y)
				toast("ս������")
				print("�����������")
				break
			end
		else
			print("û��ս������")
			ret,x,y=findPic(229,391,288,447, "ս��ȦȦ.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�ս��")
				break
			else
				��ս��()
			end
		end
	end
	while true do
		ret,x,y=findPic(229,391,288,447, "ս��ȦȦ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			tap(400,407)
			print("���5v5")
			break
		else
			print("δ�ҵ�5v5")
			sleep(1000)
			ret,x,y=findPic(393,31,456,90, "ս������.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				ret,x,y=findPic(19,1129,60,1189, "��������.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					tap(x,y)
					toast("ս������")
					print("�����������")
				else
					ret,x,y=findPic(229,391,288,447, "ս��ȦȦ.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("�ҵ���")
						tap(400,407)
						print("���5v5")
						break
					end
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(33,1135,78,1180, "ս��׼.png","101010", 0, 0.7)
		if x~=-1 and y ~=-1 then
			print("����ȴ�����ɹ�")
			sleep(2000)
			tap(x,y)
			print("����ٴ�׼��")
			sleep(8000)
			break
		else
			print("����ȴ�����ʧ��")
			sleep(1000)
			ret,x,y=findPic(83,614,113,647, "׼.png", "101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���")
				tap(x,y)
				print("���׼��")
			else
				ret,x,y=findPic(609,946,686,1019, "����.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("����ս����ս����")
					break
				else
					print("û�н���ս����ս����")
					ret,x,y=findPic(212,685,266,906,"��ɫ.png","101010",0,0.9)
					if x~=-1 and y ~=-1 then
						print("�ҵ���")
						print(x,y)
						tap(x,y)
					end
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(27,949,75,1232,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			sleep(10000)
			break
		else
			print("û�ҵ�")
			ս������()
			print("ս������")
			ret,x,y=findPic(212,685,266,906,"��ɫ.png","101010",0,0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���")
				print(x,y)
				tap(x,y)
			end
		end
	end
	while true do
		ret,x,y=findPic(0,762,264,1245,"��ɫ.png","101010",0,0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			print(x,y)
			tap(x,y)
			sleep(5000)
		else
			print("�Ҳ���")
			sleep(1000)
			ret,x,y=findPic(393,31,456,90, "ս������.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				ret,x,y=findPic(29,1130,76,1205, "��������.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					break
				end
			else
				ret,x,y=findPic(517,939,624,1096, "����.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					break
				else
					ret,x,y=findPic(229,391,288,447, "ս��ȦȦ.png","101010", 0, 0.9)
					if x~=-1 and y ~=-1 then
						print("�ҵ�ս��")
						break
					end
				end
			end
		end
	end
end
function ���������()
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
function �۽������()
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
function ��ʦ�������()
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
function ���������()
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
function ս�������()
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
function ����������()
	tap(163, 637)
	sleep(500)
	tap(94, 640)
	sleep(500)
end
function ̫��()
	while true do
		ret,x,y=findPic(17, 900, 71, 1084, "̫���ٴ���ս.png", "101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			tap(x,y)
			toast("�ٴ���ս")
			sleep(1000)
			break
		else
			ret,x,y=findPic(183,997,290,1073, "̫���.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("��ʼ����")
				tap(x,y)
				toast("��ʼ����")
				print("�������")
				sleep(1000)
				break
			else
				ret,x,y=findPic(542,948,588,1087, "����.png","101010", 0, 0.8)
				if x~=-1 and y ~=-1 then
					print("�ҵ�����")
					tap(x,y)
					print("�������")
					sleep(2000)
					tap(x,y)
					print("����ؾ�")
				else
					print("δ�ҵ�����")
					sleep(5000)
				end
			end
		end
	end
	while true do
		ret,x,y=findPic(31,550,82,733, "̫�鿪ʼ��ս.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("����ɹ�")
			tap(x, y)
			sleep(1000)
			break
		else
			print("�ȴ���")
			sleep(1000)
		end
	end
	while true do
		ret,x,y=findPic(12,1107,152,1252, "̫�鿪ʼ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			sleep(2000)
			tap(x, y)
			print("�����ʼ")
			sleep(1000)
			break
		else
			ret,x,y=findPic(313,751,375,822, "̫����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("����ɹ�")
				sleep(2000)
				if ̫��ѡ�� == "0" then
					tap(660,160)
				else
					tap(45,953)
				end
				print("���ѡ��")
				sleep(1000)
				break
			else
				print("û�ҵ�")
				sleep(1000)
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(11,394,58,447, "��.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("����̫��ɹ�")
			sleep(2000)
			break
		else
			ret,x,y=findPic(12,1107,152,1252, "̫�鿪ʼ.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				sleep(2000)
				tap(x,y)
				print("�����ʼ")
				sleep(1000)
			end
		end
	end
	while true do
		ret,x,y=findPic(56,319,159,423, "̫���Զ�.png","101010", 0, 0.8)
		if x~=-1 and y ~=-1 then
			print("�ҵ���")
			sleep(2000)
			tap(x,y)
			print("����Զ�")
			break
		else
			print("�Ҳ���")
			sleep(1000)
		end
	end
end
function ����()
	while true do
		ret,x,y=findPic(18,962,66,1133, "�콱.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ��콱���ճ�����")
			sleep(2000)
			tap(41,1074)
			sleep(1000)
			break
		else
			ret,x,y=findPic(65,330,157,409, "�Զ�.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ��Զ�")
				toast("�ҵ��Զ���������������")
				sleep(2000)
				tap(x, y)
				sleep(2000)
			end
		end
	end
end
function ��սģʽѡ��()
	if �ճ�ѡ�� == "1" then
		tap(147,626)
	elseif �ճ�ѡ�� == "0@1" then
		tap(147,626)
	elseif �ճ�ѡ�� == "0@1@4" then
		tap(147,626)
	elseif �ճ�ѡ�� == "1@4" then
		tap(147,626)
	elseif �ճ�ѡ�� == "2" then
		tap(147,825)
	elseif �ճ�ѡ�� == "0@2" then
		tap(147,825)
	elseif �ճ�ѡ�� == "0@2@4" then
		tap(147,825)
	elseif �ճ�ѡ�� == "2@4" then
		tap(147,825)
	elseif �ճ�ѡ�� == "3" then
		tap(147,1030)
	elseif �ճ�ѡ�� == "0@3" then
		tap(147,1030)
	elseif �ճ�ѡ�� == "0@3@4" then
		tap(147,1030)
	elseif �ճ�ѡ�� == "3@4" then
		tap(147,1030)
	end
end
function ��ս()
	while true do
		ret,x,y=findPic(110,552,176,612, "ǰ����ս.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("ǰ��")
			sleep(2000)
			��սģʽѡ��()
			sleep(1000)
			break
		else
			ret,x,y=findPic(542,948,588,1087, "����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				sleep(2000)
				tap(x,y)
				print("�������")
				sleep(2000)
				tap(x,y)
				print("����ؾ�")
				sleep(2000)
				tap(363, 77)
				print("�����ս")
			else
				print("δ�ҵ�����")
				sleep(5000)
			end
		end
	end
	while true do
		ret,x,y=findPic(12,1107,152,1252, "��ս��ʼ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			sleep(2000)
			tap(x, y)
			print("�����ʼ")
			sleep(1000)
			break
		else
			ret,x,y=findPic(313,751,375,822, "̫����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("����ɹ�")
				sleep(2000)
				tap(45, 953)
				print("���ѡ��")
				sleep(1000)
				break
			else
				print("û�ҵ�")
				sleep(1000)
			end
		end
	end
	while true do
		ret,x,y=findPic(60,320,152,414, "��ս�Զ����.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			sleep(2000)
			print("�����Զ���ս")
			break
		else
			ret,x,y=findPic(60,320,152,414, "��ս�Զ�.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				tap(x,y)
				sleep(2000)
			end
		end
	end
	sleep(5000)
	while true do
		ret,x,y=findPic(18,962,66,1133, "�콱.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ��콱���ճ�����")
			sleep(5000)
			tap(x,y)
			sleep(1000)
			break
		else
			print("�Ҳ����콱")
			sleep(2000)
		end
	end
	while true do
		ret,x,y=findPic(253,657,309,812, "��սȷ��.png","101010", 0, 0.8)
		if x~=-1 and y ~=-1 then
			print("�ҵ�ȷ��")
			sleep(2000)
			tap(x,y)
			sleep(1000)
			print("��ս����")
			break
		else
			ret,x,y=findPic(53,1124,167,1226, "��ս����.png","101010", 0, 0.8)
			if x~=-1 and y ~=-1 then
				print("�ҵ�����")
				sleep(2000)
				tap(x,y)
				sleep(1000)
			else
				print("û�ҳ���")
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
function ����()
	while true do
		while true do
			ret,x,y=findPic(1,385,68,448, "��.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���")
				tap(35, 98)
				sleep(1000)
				inputText(��������)
				sleep(1000)
				tap(59, 1177)
				sleep(1000)
				tap(32,497)
				print("���ͳɹ�")
				sleep(180000)
				break
			else
				ret,x,y=findPic(17,403,55,440, "��.png","101010", 0, 0.7)
				if x~=-1 and y ~=-1 then
					print("�ҵ���")
					tap(36,372)
					sleep(1000)
				end
			end
		end
	end
end
function ��ļ()
	while true do
		while true do
			ret,x,y=findPic(11,749,58,802, "������ļ.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("�ҵ���")
				tap(x, y)
				sleep(1000)
				tap(492, 871)
				sleep(1000)
				tap(156, 641)
				sleep(1000)
				tap(392, 368)
				sleep(1000)
				inputText(��������)
				sleep(1000)
				tap(59, 1177)
				sleep(1000)
				tap(165, 637)
				sleep(1000)
				print("�����ɹ�")
				break
			else
				ret,x,y=findPic(5,820,74,888, "����.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("�ҵ�����")
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
if ģʽѡ�� == "0"  then
	if ����ѡ�� == "0" then
		if ѭ������ == "0" then
			print("��ǰΪ����ģʽ")
			while true do
				����()
			end
		elseif ѭ������ > "0" then
			for i=1,ѭ������ do
				toast("������"..i.."��ѭ��")
				sleep(1000)
				����()
			end
			ѭ������()
		end
	end
	if ����ѡ�� == "1" then
		if ѭ������ == "0" then
			print("��ǰΪ�۽�ģʽ")
			while true do
				�۽�()
			end
		elseif ѭ������ > "0" then
			for i=1,ѭ������ do
				toast("�۽���"..i.."��ѭ��")
				sleep(1000)
				�۽�()
			end
			ѭ������()
		end
	end
	if ����ѡ�� == "2" then
		if ѭ������ == "0" then
			print("��ǰΪ��ʦ��ģʽ")
			while true do
				��ʦ��()
			end
		elseif ѭ������ > "0" then
			for i=1,ѭ������ do
				toast("��ʦ����"..i.."��ѭ��")
				sleep(1000)
				��ʦ��()
			end
			ѭ������()
		end
	end
	if ����ѡ�� == "3" then
		if ѭ������ == "0" then
			print("��ǰΪ����ģʽ")
			while true do
				����()
			end
		elseif ѭ������ > "0" then
			for i=1,ѭ������ do
				toast("���ǵ�"..i.."��ѭ��")
				sleep(1000)
				����()
			end
			ѭ������()
		end
	end
	if ����ѡ�� == "4" then
		if ѭ������ == "0" then
			print("��ǰΪս��ģʽ")
			while true do
				ս��()
			end
		elseif ѭ������ > "0" then
			for i=1,ѭ������ do
				toast("ս����"..i.."��ѭ��")
				sleep(1000)
				ս��()
			end
			ѭ������()
		end
	end
elseif ģʽѡ�� == "1" then
	if ����ѡ�� == "0" then
		while true do
			���������()
		end
	end
	if ����ѡ�� == "1" then
		while true do
			�۽������()
		end
	end
	if ����ѡ�� == "2" then
		while true do
			��ʦ�������()
		end
	end
	if ����ѡ�� == "3" then
		while true do
			���������()
		end
	end
	if  ����ѡ�� == "4" then
		while true do
			ս�������()
		end
	end
	if ����ѡ�� == "5" then
		while true do
			����������()
		end
	end
elseif ģʽѡ�� == "2" then
	print("��ǰΪ̫��ģʽ")
	if ѭ������ == "0" then
		while true do
			̫��()
		end
	elseif ѭ������ > "0" then
		for i=1,ѭ������ do
			toast("̫���"..i.."��ѭ��")
			sleep(1000)
			̫��()
		end
		ѭ������()
	end
end
if ģʽѡ�� == "3" then
	if �ճ�ѡ�� == "1" then
		��ս()
	elseif �ճ�ѡ�� == "0@1" then
		����()
		sleep(3000)
		��ս()
	elseif �ճ�ѡ�� == "0@1@4" then
		����()
		sleep(3000)
		��ս()
		sleep(3000)
		̫��()
	elseif �ճ�ѡ�� == "1@4" then
		��ս()
		sleep(3000)
		̫��()
	elseif �ճ�ѡ�� == "2" then
		��ս()
	elseif �ճ�ѡ�� == "0@2" then
		����()
		sleep(3000)
		��ս()
	elseif �ճ�ѡ�� == "0@2@4" then
		����()
		sleep(3000)
		��ս()
		sleep(3000)
		̫��()
	elseif �ճ�ѡ�� == "2@4" then
		��ս()
		sleep(3000)
		̫��()
	elseif �ճ�ѡ�� == "3" then
		��ս()
	elseif �ճ�ѡ�� == "0@3" then
		����()
		sleep(3000)
		��ս()
	elseif �ճ�ѡ�� == "0@3@4" then
		����()
		sleep(3000)
		��ս()
		sleep(3000)
		̫��()
	elseif �ճ�ѡ�� == "3@4" then
		��ս()
		sleep(3000)
		̫��()
	elseif �ճ�ѡ�� == "0" then
		����()
	elseif �ճ�ѡ�� == "4" then
		̫��()
	end
	while true do
		ret,x,y=findPic(19,1146,64,1191, "̫���˳�.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			tap(x,y)
			print("�˳�̫��ɹ�")
			sleep(2000)
			break
		else
			print("�˳�̫��ʧ��")
		end
	end
	while true do
		ret,x,y=findPic(457,1076,540,1154, "����.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ�����")
			sleep(2000)
			tap(x,y)
			sleep(1000)
			break
		else
			print("û�ҵ�����")
			sleep(2000)
		end
	end
	while true do
		ret,x,y=findPic(142,160,197,694, "��ȡ.png","101010", 0, 0.9)
		if x~=-1 and y ~=-1 then
			print("�ҵ���ȡ")
			sleep(2000)
			tap(x,y)
			sleep(1000)
		else
			ret,x,y=findPic(521,290,635,1123, "����.png","101010", 0, 0.9)
			if x~=-1 and y ~=-1 then
				print("��ȡ���")
				sleep(2000)
				tap(x,y)
				sleep(1000)
			else
				ret,x,y=findPic(480,990,621,1123, "1000.png","101010", 0, 0.9)
				if x~=-1 and y ~=-1 then
					print("ֹͣ")
					sleep(2000)
					break
				end
			end
		end
	end
end
if ģʽѡ�� == "4" then
	if ����ѡ�� == "0" then
		����()
	end
	if ����ѡ�� == "1" then
		��ļ()
	end
end

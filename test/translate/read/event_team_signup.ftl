<#-- @ftlvariable name="applyCountMin" type="int" -->
<#-- @ftlvariable name="maxUsePointsMoney" type="int" -->
<#include "inc/cfg.ftl">

<#global
page_title = "活动报名"
page_name = "event-signup-team"
assets_css = ["font-awesome", "bootstrap-datepicker", "fileicons"]
page_css = ["signup"]
price = eventStyle.price + serviceTotalPrice
event = eventInfo
batch = eventStyle
>
<#assign 
	isHuwai = sas_site_type == "huwai"
	useDeposit = useDeposit!'N'
	depositUnitPrice = depositUnitPrice!0
	maxPointsUse = maxUsePoints!0
	pointsGet = userGetPoints
	unitPrice = memberUnitPrice
/>
<#if useDeposit == 'Y'>
	<#assign unitPrice = depositUnitPrice>
</#if>
<#include "inc/head.ftl">
<body><#escape x as x?html>
<#include "inc/header.ftl">
<div class="apply-wrap u-main u-box u-mode">

	<#include "inc/_event_signup_info.ftl">

	<div class="applicant-title u-title3">
		报名人信息
		<span>（本活动的相关通知会通知联系人, 请留意手机短信并准确填写报名人信息，以便办理各种手续和购买保险，
		团队报名人数范围为
			<#if applyCountMax gt 0>
				<#if applyCountMin == applyCountMax>
				${applyCountMin}
				<#else>
				${applyCountMin} - ${applyCountMax}
				</#if>
                人
			<#else>
			${applyCountMin} 人以上
			</#if>
		）</span>
	</div>
	<ul class="applicant-data-list">
		<li>
            <h4 class="theme-bgcolor">联系人信息
				<s class="theme-border2 top-right"></s><i class="theme-border left"></i></h4>
            <form>
				<div class="form-data">
                    <div class="form-line form-group require">
						<label for="contactName" class="form-label">联系人姓名：</label>
						<input type="text" name="trueName" validator="required" maxlength="20" class="form-control"
							   id="contactName" placeholder="1-20个字符" value="${(userExt.trueName)!}">
					</div>
                    <div class="form-line form-group require">
						<label for="contactPhone" class="form-label">手机号码：</label>
						<input type="text" name="mobile" validator="required|mobile" maxlength="11" class="form-control"
							   id="contactPhone" placeholder="请输入11位手机号码" value="${(user.phone)!}">
						<#if !userLogged>
                            <button type="button" id="getCode" class="theme-bgcolor fl">获取验证码</button>
						</#if>
					</div>
					<#if !userLogged>
                        <div class="form-line form-group require">
                            <label for="checkCode" class="form-label">手机校验码：</label>
                            <input type="text" name="mobile" validator="required" maxlength="6"  class="form-control"
                                   id="phoneCode" placeholder="请输入手机校验码" >
                        </div>
					</#if>
				</div>
			</form>
		</li>
        <li>
            <h4 class="theme-bgcolor">团队成员信息
                <s class="theme-border2 top-right"></s><i class="theme-border left"></i>
			</h4>
			<div class="team-apply-step">
                <span class="fl">第一步：团队名称： </span>
				<input type="text" placeholder="为你的团队取个名字吧！" id="teamName" name="teamName" style="width: 324px"
					   maxlength="50" class="form-control">
			</div>
			<#if applyCountMin == applyCountMax>
             	<div class="team-apply-step">第二步：参加的团队人数${applyCountMin}人</div>
                <input type="hidden" value="${applyCountMin}" id="team-apply-num">
			<#else>
				<div class="team-apply-step">
					<span class="fl">第二步：参加的团队人数（范围：${applyCountMin} - ${applyCountMax}人） &nbsp;</span>
					<input placeholder="${applyCountMin} - ${applyCountMax}人" type="text" class="form-control"
						   value="${applyCountMin}" id="team-apply-num"  style="width: 100px"
						   data-min="${applyCountMin}" data-max="${applyCountMax}"/>
				</div>
			</#if>

            <div class="team-apply-step">第三步：点击这里下载成员信息文件模板， <a href="/event/teamapply/doc?activityId=${event.id}"><#if currentSas.languageSupport == 'C'>团队成员信息模板文件.xls<#else>Team member information input template file.xls</#if></a></div>

            <div class="team-apply-step ovl">
				<span class="fl">第四步：</span>
				<div id="uploader-team-wrap" class="fl">
					<a class="upload-team-file btn btn-primary" id="upload-team-file">+上传成员信息文件</a>
        		</div>
                <a href="javascript:;" download="" target="_blank" id="team-file-link"></a>
			</div>
		</li>
	</ul>
	<#if event.applyAttachmentState != 'N'>
    <div class="u-title3">
	    报名附件
	    <small>
		    <#if (event.attachmentDesc)?has_content>
			    （${event.attachmentDesc}）
		    </#if>
        </small>
    </div>
		<div class="other-field">
			<#if event.applyAttachmentState != 'N'>
				<div class="att-list field-line">
					<label for="">上传附件：</label>
					<a href="javascript:;" class="add-att" id="uploader-att">+ 添加附件</a>

				</div>
				<div class="att att-template" data-id="" data-state="${event.applyAttachmentState}" style="display: none">
					<span class="fileicon"></span>
					<span class="name"></span>
					<span class="size"></span>
					<span class="progress"><div></div></span>
					<span class="progress-num c9"></span>
					<a href="javascript:;" class="close c3">×</a>
				</div>
			</#if>
		</div>
	</#if>
    <div class="u-title3" style="margin-top: 40px;">其他信息</div>
	<div class="other-field">
		<div class="field-line">
            <label for="remark">订单备注：</label>
            <textarea id="remark" class="remark"></textarea>
		</div>
	</div>

	<#if event.protocolState == 'N'>
        <div class="select-line">
            <input type="checkbox" checked id="agree">
            <label for="agree">我已阅读并同意</label>
            <a href="${cfg_root_path}/event/terms?id=${event.id}&styleClassId=${batch.id}&applyMethodType=T"
               target="_blank" class="theme-color">《报名条款》</a>
        </div>
	</#if>
	<#assign minPrice = unitPrice * applyCountMin>
	<@points_credit points=maxPointsUse money=minPrice/>

	<#assign minPrice = unitPrice * applyCountMin>
	<@payInfo total_price=minPrice credit_money=maxUsePointsMoney use_deposit=useDeposit=='Y'
	support_pay_offline=batch.payType == 'O'
	/>
</div>
<#include 'inc/_captcha_window.ftl'>
<input type="hidden" data-id="${event.id}" data-count="${applyCountMin}" data-batch="${batch.id}" id="j-data"/>
<#include "inc/footer.ftl">
<#include "inc/scripts.ftl">
<script src="${cfg_assets_path}/js/lib/bootstrap.js?${cfg_version}"></script>
<script src="${cfg_assets_path}/js/lib/bootstrap.datepicker.js?${cfg_version}"></script>
<script src="${cfg_assets_path}/js/fw/utilities/datetimeselect.js?${cfg_version}"></script>
<script src="${cfg_assets_path}/js/lib/plupload.full.js?${cfg_version}"></script>
<script src="${cfg_assets_path}/js/lib/qiniu.js?${cfg_version}"></script>

</#escape>
<script>
	<#if event.applyAttachmentState != 'N'>
	window.uploadEnabled= true;
	</#if>
    var eventId= '${event.id}',
            eventStyleId = '${batch.id}',
            eventServiceIds = "${serviceIds}",

            maxUsePointsMoney = ${maxUsePointsMoney},
            memberUnitPrice = ${memberUnitPrice},
            deposit = ${depositUnitPrice},
            unitPrice = ${unitPrice},

            pointsGet = ${pointsGet},
            useDeposit = '${useDeposit}',
            maxPointsUse = ${maxPointsUse};
</script>
</body>
</html>

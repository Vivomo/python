<#-- @ftlvariable name="memberUnitPrice" type="int" -->
<#-- @ftlvariable name="maxUsePointsMoney" type="int" -->
<#include "inc/cfg.ftl">

<#global
page_title = "活动报名"
page_name = "event-signup"
assets_css = ["font-awesome", "bootstrap-datepicker", "fileicons"]
page_css = ["signup"]
batch = eventStyle
price = batch.price + serviceTotalPrice
event = eventInfo

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
<div class="apply-wrap u-main u-box">
	<#include "inc/_event_signup_info.ftl">

	<div class="applicant-title u-title3">
		报名人信息<span>（本活动的相关通知会通知第1个报名人, 请留意手机短信并准确填写报名人信息，以便办理各种手续和购买保险，最多添加
		<span id="max-applier">${event.maxApplier}</span>个）</span>
	</div>
	<ul class="applicant-data-list" id="applicantList"></ul>
	<ul class="template">
        <li>
	        <#if event.maxApplier == 1>
	            <h4 class="theme-bgcolor" style="min-width: 72px;">报名信息<s class="theme-border2 top-right"></s><i class="theme-border left"></i></h4>
	        <#else>
	            <h4 class="theme-bgcolor">第<span class="num"></span>个报名人
		            <s class="theme-border2 top-right"></s><i class="theme-border left"></i></h4>
	        </#if>
            <span class="remove-applier">×</span>
            <form><div class="form-data"></div></form>
        </li>
	</ul>
	<button class="j-add theme-bgcolor" id="addApplierBtn">+新增报名人员</button>
    <#--<div class="u-title3">其他信息</div>-->
	<#if event.applyAttachmentState != 'N'>
    <div class="u-title3">报名附件
	    <small>
		    <#if (event.attachmentDesc)?has_content>
			    （${event.attachmentDesc}）
		    </#if>
        </small>
    </div>
	<div class="other-field"  style="margin-bottom: 40px;">
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
	</div>
	</#if>
	<div class="other-field">
		<div class="u-title3">其他信息</div>
		<div class="field-line">
			<label for="remark">订单备注：</label>
			<textarea id="remark" class="remark"></textarea>
		</div>

		<#if event.protocolState == 'N'>
		<div class="select-line">
			<input type="checkbox" checked id="agree">
			<label for="agree">我已阅读并同意</label>
			<a href="${cfg_root_path}/event/terms?id=${event.id}&styleClassId=${batch.id}&applyMethodType=U"
					  target="_blank" class="theme-color">《报名条款》</a>
	    </div>
		</#if>

		<@points_credit points=maxPointsUse money=maxUsePointsMoney/>
	</div>

	<@payInfo total_price=unitPrice credit_money=maxUsePointsMoney use_deposit=useDeposit=='Y'
		support_pay_offline=batch.payType == 'O'
	/>

</div>


<input type="hidden" data-id="${event.id}" data-batch="${batch.id}" id="j-data"/>
<textarea id="anonymous-html" style="display: none">
	<div class="form-line anonymous-line require clearfix">
		<label for="id_128_1" class="form-label">手机号码：</label>
		<input type="text" class="form-control" validator="required" name="mobile" maxlength="11" id="id_128_1" placeholder="请输入手机号码">
		<button id="getCode" type="button" class="fl theme-bgcolor">获取验证码</button>

		<label for="checkCode" class="form-label">手机验证码：</label>
		<input type="text" validator="required" class="form-control" id="checkCode" placeholder="请输入短信验证码">
	</div>
</textarea>
<#include 'inc/_captcha_window.ftl'>
<#include "inc/footer.ftl">
<script>
    var eventId= ${event.id},
		useDeposit = '${useDeposit!"N"}',
		memberUnitPrice = ${memberUnitPrice},
		unitPrice = ${unitPrice},
		eventStyleId = ${batch.id},
		eventServiceIds = "${serviceIds}",
		maxUsePointsMoney = ${maxUsePointsMoney},
		deposit = parseFloat('${depositUnitPrice}'),
		pointsGet = parseFloat('${pointsGet}'),
		maxPointsUse = ${maxPointsUse};

</script>
<#include "inc/scripts.ftl">
<script src="${cfg_assets_path}/js/lib/city.min.js"></script>
<script src="${cfg_assets_path}/js/lib/cityselect.js"></script>
<script src="${cfg_assets_path}/js/lib/bootstrap.js?${cfg_version}"></script>
<script src="${cfg_assets_path}/js/lib/bootstrap.datepicker.js?${cfg_version}"></script>
<script src="${cfg_assets_path}/js/fw/utilities/datetimeselect.js?${cfg_version}"></script>

<#if event.applyAttachmentState != 'N'>
<script>
	window.uploadEnabled= true;
</script>
<script src="${cfg_assets_path}/js/lib/plupload.full.js?${cfg_version}"></script>
<script src="${cfg_assets_path}/js/lib/qiniu.js?${cfg_version}"></script>

</#if>

</#escape></body>
</html>

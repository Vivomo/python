<#include "inc/cfg.ftl">
<#global lang_name='event' >
<#global
page_title = "${l_order}"
page_name = "event-order"
page_css = [page_name]
assets_css = ['fileicons']
order = orderInfo
attList = orderAttachments![]
event = eventInfo
serviceTitles = order.additionalServiceTitles
state = orderStateInfo
canDel = state == 0
free = order.totalPriceWithRefundAmount == 0
canCancel = state != 0 && state != 100 && !(state > 20 && !free)
canPay = pay_enable && state == 20
canDel = state == 0
isPayAll = order.orderDepositType == 'N'
isUserPrice = order.orderPriceType == "N"
>
<#assign isHuwai = sas_site_type == "huwai" />
<#include "inc/head.ftl">
<body><#escape x as x?html>
<#include "inc/header.ftl">
<#if action_state??>
<input type="hidden" data-num="${action_state}" id="alert_msg" value="${action_msg!''}">
</#if>

<div class="order-wrap u-main u-box u-mode">
	<h1 class="u-title t-c">${l_event_order_detail}</h1>
    <div class="order-state">
        <#--<label for="">${l_order_status}：</label>-->
        <ul <#if state == 0>style="left: 710px;"<#else>style="left: 320px;"</#if>>

            <li>
                <div class="state theme-color-act  <#if state gte 10 >active</#if>">${l_event_apply}</div>
                <div class="num theme-bgcolor-act theme-border-act  <#if state gte 10 >active</#if>">1</div>
            </li>
			<#if state == 0>
                <li style="border: 0">
                    <div class="state theme-color-act active">${l_order_is_closed}</div>
                    <div class="num theme-bgcolor-act theme-border-act active">2</div>
                </li>
			<#else>
                <li <#if !(isOwner || isAdmin)>style="border: 0" </#if> >
                    <div class="state theme-color-act  <#if state gte 20>active</#if>">${l_censor_pass}</div>
                    <div class="num theme-bgcolor-act theme-border-act  <#if state gte 20>active</#if>">2</div>
                </li>
				<#if isOwner || isAdmin>
                    <li>
                        <div class="state theme-color-act  <#if state gte 30>active</#if>"><#if !pay_enable>${l_already_paid}（${l_offline_payment}）<#else>${l_already_paid}</#if></div>
                        <div class="num theme-bgcolor-act theme-border-act  <#if state gte 30>active</#if>">3</div>
                    </li>
                    <li>
                        <div class="state theme-color-act  <#if state gte 40>active</#if>">${l_event_is_ongoing}/${l_join_the_event}</div>
                        <div class="num theme-bgcolor-act theme-border-act  <#if state gte 40>active</#if>">4</div>
                    </li>
                    <li style="border: 0">
                        <div class="state theme-color-act <#if state gte 100>active</#if>">${l_trade_success}</div>
                        <div class="num theme-bgcolor-act  <#if state gte 100>active</#if> theme-border-act">5</div>
                    </li>
				</#if>
			</#if>
        </ul>
    </div>
	<a class="title theme-color" href="${cfg_root_path}/event?id=${eventInfo.id}">${eventInfo.title}</a>
	<#if isOwner>
		<#if state == 0>
            <div class="attention theme-border">
                ${l_current_order_status}：<strong>${l_has_been_canceled}</strong>
				<button class="button button-danger button-master button-s del" data-id="${order.id}">${l_delete_order}</button>
            </div>
		<#elseif state == 10>
            <div class="attention theme-border">
                ${l_current_order_status}：<strong>${l_order_censoring}</strong>
                <a href="javascript:;" class="slave-pen cancel">${l_cancel_order}</a>
            </div>
		<#elseif state == 20>
            <#if canPay>
                <div class="attention theme-border">
                    ${l_current_order_status}：<strong>${l_censor_pass}，${l_please_pay_in_time}。</strong>
                    <a href="javascript:;" class="slave-pen cancel">${l_cancel_order}</a>
                    <#--<button class="button button-master button-s theme-bgcolor" id="payButtonSmall">${l_pay}</button>-->
	                <#if order.orderPayType == 31>
	                <strong>${l_the_event_is_paid_offline}</strong>
	                <#else>
		                <button class="button button-master button-s theme-bgcolor" id="payButtonSmall">${l_pay}</button>
	                </#if>
                </div>
            <#else>
                <div class="attention theme-border">
                    ${l_current_order_status}：<strong>${l_censor_pass}，${l_payment_is_not_supported}，${l_please_pay_offline}。</strong>
                    <a href="javascript:;" class="slave-pen cancel">${l_cancel_order}</a>
                    <button class="button button-master button-s theme-bgcolor" id="payButtonSmall" disabled style="background-color: #ccc !important;cursor: not-allowed;">${l_pay}</button>
                </div>
            </#if>
		<#elseif state == 30>
            <div class="attention theme-border">
                ${l_current_order_status}：<strong>${l_paid_successfully}<#if !pay_enable>（${l_offline_payment}）</#if>，${l_please_be_patient_and_wait_for_event_notification}。</strong>
                <#if canCancel || (order.depositePrice == 0 && order.orderDepositType =='Y')>
                    <a href="javascript:;" class="slave-pen cancel">${l_cancel_order}</a>
                </#if>
            </div>
		<#elseif state == 40 && order.totalPriceWithRefundAmount == 0>
            <div class="attention theme-border">
                ${l_current_order_status}：<strong>${l_event_is_ongoing}。</strong>
                <#if canCancel>
				<a href="javascript:;" class="slave-pen cancel">${l_cancel_order}</a>
                </#if>
            </div>
		<#elseif state == 100>
            <div class="attention theme-border">
                ${l_current_order_status}：<strong>${l_trade_success}，${l_thank_you_for_your_applying.}。</strong>
            </div>
		</#if>
	</#if>
	<h3 class="u-title3">${l_order_details}</h3>
	<div class="order-data">
		<div class="data-line">
			<span class="key">订&ensp;单&ensp;号：</span>
			<div class="value theme2-color order-code">${order.orderCode}</div>
		</div>
		<div class="data-line">
			<span class="key">${l_order_time}：</span>
			<div class="value">${formatDate(order.createTime, 'yyyy-MM-dd HH:mm')}</div>
		</div>
		<div class="data-line">
			<span class="key">${l_apply_method}：</span>
			<div class="value">${applyMethodType}</div>
		</div>
		<div class="data-line">
			<span class="key">${l_payment_method}：</span>
			<div>${isPayAll?string('${l_full_payment}','${l_deposit_payment}')}</div>
		</div>
		<#if order.useCreditPointCount != 0 ><#--&& !(order.refundAmount gt 0)-->
			<div class="data-line">
				<span class="key">${l_integral_deduction}：</span>
				<div>${l_use}<span class="theme2-color"> ${order.useCreditPointCount} </span>${l_integral}，${l_deduction}<span class="theme2-color"> &yen;${order.useCreditPointPrice} </span>${l_yuan}</div>
			</div>
		</#if>
		<#if order.refundAmount gt 0 && order.useCreditPointCount != 0>
			<div class="data-line">
				<span class="key">${l_integral_return}：</span>
				<div>${l_has_returned}<span class="theme2-color"> ${order.useCreditPointCount} </span>${l_integral_deposited_into_your_account}</div>
			</div>
		</#if>
		<div class="data-line">
			<span class="key">${l_total_amount}：</span>
			<div class="theme2-color">&yen;${order.totalPriceWithRefundAmount}<#if !isPayAll>（${l_deposit} &yen;${order.depositePrice} + ${l_balance} &yen;${order.totalRemainderPrice}）</#if></div>
		</div>
		<div class="data-line">

			<#if state == 30 || state == 40 || state == 100>
				<span class="key" id="sas-js-custom-modification-event-prices">${l_actual_amount}：</span>
				<div class="sas-js-no-margin-left no-margin-left">
					<span class="theme2-color">
						<#if isPayAll>
							&yen;${order.totalPriceWithRefundAmount!0}
							<#if order.totalPriceWithRefundAmount !=0 >
								<#if  order.orderPayType == 31 || order.orderPayType == 1>
									（${l_offline_payment}<#if order.refundAmount gt 0 > ${l_refunded} ${order.refundAmount} ${l_yuan}</#if>）
								<#else>
									（${l_online_payment}<#if order.refundAmount gt 0 > ${l_refunded} ${order.refundAmount} ${l_yuan}</#if>）
								</#if>
							</#if>
					    <#else>
						    &yen;${(order.depositePrice)!0}
						    <#if order.refundAmount gt 0 >
							    （${l_refunded} ${order.refundAmount} ${l_yuan}）
						    </#if>
						</#if>
					</span>
				</div>
			<#else>
				<span class="key" id="sas-js-custom-modification-event-prices">${l_amount_to_pay}：</span>
				<div class="sas-js-no-margin-left no-margin-left">
					<span class="theme2-color">
						<#if isPayAll>
							&yen;${order.totalRemainderPrice!0}
							<#if order.totalRemainderPrice !=0 >
								<#if  order.orderPayType == 31 || order.orderPayType == 1>
									（${l_offline_payment}）
								<#else>
									（${l_online_payment}）
								</#if>
							</#if>
						<#else>
							&yen;${(order.depositePrice)!0}

						</#if>
						<#if order.refundAmount gt 0 >
							（${l_refunded} ${order.refundAmount} ${l_yuan}）
						</#if>
					</span>
				</div>
			</#if>
		</div>

	<#if order.getCreatePointCount != 0>
		<div class="data-line">
			<span class="key">${l_integral_presentation}：</span>
			<div>${l_trade_success}送<span class="theme2-color"> ${order.getCreatePointCount} </span>${l_integral}</div>
		</div>
	</#if>

		<div class="clear"></div>

	</div>

	<div class="u-title3">${l_information}</div>
	<div class="order-data">
		<#if !((event.sourceProvince == "${l_overseas}" || event.sourceProvince == "${l_other}") && event.sourceDetailAddress == '')>
        <div class="data-line">
            <span class="key">集&ensp;合&ensp;地：</span>
            <div class="value">${formatAddress2(event,1)}</div>
        </div>
		</#if>
		<#if !((event.destProvince == "${l_overseas}" || event.destProvince == "${l_other}") && event.destDetailAddress == '')>
        <div class="data-line">
            <span class="key">目&ensp;的&ensp;地：</span>
            <div class="value">${formatAddress2(event,2)}</div>
        </div>
		</#if>
        <div class="data-line">
            <span class="key">${isHuwai?string("${l_start_date}","${l_start_date}")}：</span>
            <div class="value">${formatDate(event.startTime, "yyyy-MM-dd")}</div>
        </div>
        <div class="data-line">
            <span class="key">${l_end_date}：</span>
            <div class="value">${formatDate(event.endTime, 'yyyy-MM-dd')}</div>
        </div>
        <div class="data-line">
            <span class="key">${isHuwai?string("${l_select_batch}","${l_select_group}")}：</span>
            <div class="value">${order.activityStyleClassTitle}</div>
        </div>
        <div class="data-line">
            <span class="key" id="sas-js-custom-modification-event">${isUserPrice?string('单　　价','${l_member_price}')}：</span>
            <div class="value theme2-color sas-js-custom-modification-event">¥${order.activityUnitPrice}</div>
        </div>
		<#if serviceTitles != ''>
            <div class="data-line2 clear">
                <span class="key">${l_additional_services}：</span>
                <div class="value">${serviceTitles}</div>
            </div>
		</#if>
	</div>
	<div class="u-title3">${l_order_contact}<span></span></div>
	<div class="order-data">
		<div class="data-line">
			<div class="key">${l_full_name}：</div>
			<div class="value">${order.contactTrueName}</div>
		</div>
		<div class="data-line">
			<div class="key">${l_mobile_phone}：</div>
			<div class="value">${order.contactPhone}</div>
		</div>
	</div>
	<#if appliers?size gt 0>
	<div class="u-title3">${l_applicant_information}<span></span></div>
	<ul class="applicants">
		<#if appliers?size == 1>
			<#list appliers as applier>
				<li>
					<div class="order-data">
						<#list applier as field>
							<div class="data-line">
								<div class="key">${field.key!''}：</div>
								<div class="value">${(field.value)!''}</div>
							</div>
						</#list>
					</div>
				</li>
			</#list>
		<#else>
			<#list appliers as applier>
				<li>
					<h5 class="theme-color">第${applier_index+1}位报名人</h5>
					<div class="order-data">
						<#list applier as field>
							<div class="data-line">
								<div class="key">${field.key!''}：</div>
								<div class="value">${(field.value)!''}</div>
							</div>
						</#list>
					</div>
				</li>
			</#list>
		</#if>

	</ul>
	</#if>

    <div class="u-title3">${l_other_information}</div>
    <div class="other-field">

		<#if order.teamApplierInfoUrl != ''>
            <div class="field-line">
                <label for="">${l_team_member_info_file}：</label>
				<a class="att" href="${order.teamApplierInfoUrl}" download="${l_team_member_information}">
					<span class="fileicon fileicon-xls"></span>
					<span class="name c6"><#if currentSas.languageSupport == 'C'>${l_team_member_information}.xls<#else>Team member information.xls</#if></span>
				</a>
            </div>
		</#if>
		<#if attList?size gt 0>
            <div class="field-line">
                <label for="">${l_attachments}：</label>
				<div class="att-list" style="margin-left: 90px;">
				<#list attList as att>
                    <a class="att" href="${att.url}" download="${att.name}">
                        <span class="fileicon fileicon-${getFileExt(att.name)}"></span>
                        <span class="name c6">${att.name}</span>
                        <span class="size c9">${getFileSize(att.size)}</span>
                    </a>
				</#list>
                </div>
            </div>
		</#if>
        <div class="field-line">
            <label for="remark">${l_order_remark}：</label>
            <div class="remind">${(order.userRemark!="")?string(order.userRemark,'无')}</div>
        </div>
    </div>

	<#if (eventInfo.imGroupQRCode)?has_content>
        <div class="u-title3">${l_event_wechat_group}<small>（${l_using_wechat_to_scan_the_qrcode_to_join_the_group}，${l_get_real_time_notification}）</small></div>
		<div style="margin:10px 0 0 12px;">
			<img src="${eventInfo.imGroupQRCode}" width="200" height="200" id="groupQRCode" />
		</div>
	</#if>
</div>
<#include "inc/footer.ftl">
<script>
    var orderId = ${order.id};
	var orderCode = '${order.orderCode}';
    var orderResult = '${action_state_ext!}';
</script>
<#include "inc/scripts.ftl">
</#escape></body>
</html>


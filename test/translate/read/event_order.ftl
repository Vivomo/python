<#include "inc/cfg.ftl">

<#global
page_title = "订单"
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
	<h1 class="u-title t-c">活动订单详情</h1>
    <div class="order-state">
        <#--<label for="">订单状态：</label>-->
        <ul <#if state == 0>style="left: 710px;"<#else>style="left: 320px;"</#if>>

            <li>
                <div class="state theme-color-act  <#if state gte 10 >active</#if>">活动报名</div>
                <div class="num theme-bgcolor-act theme-border-act  <#if state gte 10 >active</#if>">1</div>
            </li>
			<#if state == 0>
                <li style="border: 0">
                    <div class="state theme-color-act active">交易已关闭</div>
                    <div class="num theme-bgcolor-act theme-border-act active">2</div>
                </li>
			<#else>
                <li <#if !(isOwner || isAdmin)>style="border: 0" </#if> >
                    <div class="state theme-color-act  <#if state gte 20>active</#if>">审核通过</div>
                    <div class="num theme-bgcolor-act theme-border-act  <#if state gte 20>active</#if>">2</div>
                </li>
				<#if isOwner || isAdmin>
                    <li>
                        <div class="state theme-color-act  <#if state gte 30>active</#if>"><#if !pay_enable>已付款（线下付款）<#else>已付款</#if></div>
                        <div class="num theme-bgcolor-act theme-border-act  <#if state gte 30>active</#if>">3</div>
                    </li>
                    <li>
                        <div class="state theme-color-act  <#if state gte 40>active</#if>">现场领票/参加活动</div>
                        <div class="num theme-bgcolor-act theme-border-act  <#if state gte 40>active</#if>">4</div>
                    </li>
                    <li style="border: 0">
                        <div class="state theme-color-act <#if state gte 100>active</#if>">交易成功</div>
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
                当前订单状态：<strong>已取消</strong>
				<button class="button button-danger button-master button-s del" data-id="${order.id}">删除订单</button>
            </div>
		<#elseif state == 10>
            <div class="attention theme-border">
                当前订单状态：<strong>订单审核中</strong>
                <a href="javascript:;" class="slave-pen cancel">取消订单</a>
            </div>
		<#elseif state == 20>
            <#if canPay>
                <div class="attention theme-border">
                    当前订单状态：<strong>审核通过，请及时付款。</strong>
                    <a href="javascript:;" class="slave-pen cancel">取消订单</a>
                    <#--<button class="button button-master button-s theme-bgcolor" id="payButtonSmall">付款</button>-->
	                <#if order.orderPayType == 31>
	                <strong>该活动是线下支付</strong>
	                <#else>
		                <button class="button button-master button-s theme-bgcolor" id="payButtonSmall">付款</button>
	                </#if>
                </div>
            <#else>
                <div class="attention theme-border">
                    当前订单状态：<strong>审核通过，不支持支付，请线下付款。</strong>
                    <a href="javascript:;" class="slave-pen cancel">取消订单</a>
                    <button class="button button-master button-s theme-bgcolor" id="payButtonSmall" disabled style="background-color: #ccc !important;cursor: not-allowed;">付款</button>
                </div>
            </#if>
		<#elseif state == 30>
            <div class="attention theme-border">
                当前订单状态：<strong>您已付款<#if !pay_enable>（线下付款）</#if>，请耐心等待活动通知。</strong>
                <#if canCancel || (order.depositePrice == 0 && order.orderDepositType =='Y')>
                    <a href="javascript:;" class="slave-pen cancel">取消订单</a>
                </#if>
            </div>
		<#elseif state == 40 && order.totalPriceWithRefundAmount == 0>
            <div class="attention theme-border">
                当前订单状态：<strong>活动已出票。</strong>
                <#if canCancel>
				<a href="javascript:;" class="slave-pen cancel">取消订单</a>
                </#if>
            </div>
		<#elseif state == 100>
            <div class="attention theme-border">
                当前订单状态：<strong>交易成功，感谢您的报名。</strong>
            </div>
		</#if>
	</#if>
	<h3 class="u-title3">订单详情</h3>
	<div class="order-data">
		<div class="data-line">
			<span class="key">订&ensp;单&ensp;号：</span>
			<div class="value theme2-color order-code">${order.orderCode}</div>
		</div>
		<div class="data-line">
			<span class="key">下单时间：</span>
			<div class="value">${formatDate(order.createTime, 'yyyy-MM-dd HH:mm')}</div>
		</div>
		<div class="data-line">
			<span class="key">报名方式：</span>
			<div class="value">${applyMethodType}</div>
		</div>
		<div class="data-line">
			<span class="key">付款方式：</span>
			<div>${isPayAll?string('全额付款','预付定金')}</div>
		</div>
		<#if order.useCreditPointCount != 0 ><#--&& !(order.refundAmount gt 0)-->
			<div class="data-line">
				<span class="key">积分抵扣：</span>
				<div>使用<span class="theme2-color"> ${order.useCreditPointCount} </span>积分，抵扣<span class="theme2-color"> &yen;${order.useCreditPointPrice} </span>元</div>
			</div>
		</#if>
		<#if order.refundAmount gt 0 && order.useCreditPointCount != 0>
			<div class="data-line">
				<span class="key">积分返还：</span>
				<div>已返还<span class="theme2-color"> ${order.useCreditPointCount} </span>积分到账户</div>
			</div>
		</#if>
		<div class="data-line">
			<span class="key">总金额：</span>
			<div class="theme2-color">&yen;${order.totalPriceWithRefundAmount}<#if !isPayAll>（定金 &yen;${order.depositePrice} + 余款 &yen;${order.totalRemainderPrice}）</#if></div>
		</div>
		<div class="data-line">

			<#if state == 30 || state == 40 || state == 100>
				<span class="key" id="sas-js-custom-modification-event-prices">实付金额：</span>
				<div class="sas-js-no-margin-left no-margin-left">
					<span class="theme2-color">
						<#if isPayAll>
							&yen;${order.totalPriceWithRefundAmount!0}
							<#if order.totalPriceWithRefundAmount !=0 >
								<#if  order.orderPayType == 31 || order.orderPayType == 1>
									（线下支付<#if order.refundAmount gt 0 > 已退款 ${order.refundAmount} 元</#if>）
								<#else>
									（在线支付<#if order.refundAmount gt 0 > 已退款 ${order.refundAmount} 元</#if>）
								</#if>
							</#if>
					    <#else>
						    &yen;${(order.depositePrice)!0}
						    <#if order.refundAmount gt 0 >
							    （已退款 ${order.refundAmount} 元）
						    </#if>
						</#if>
					</span>
				</div>
			<#else>
				<span class="key" id="sas-js-custom-modification-event-prices">应付金额：</span>
				<div class="sas-js-no-margin-left no-margin-left">
					<span class="theme2-color">
						<#if isPayAll>
							&yen;${order.totalRemainderPrice!0}
							<#if order.totalRemainderPrice !=0 >
								<#if  order.orderPayType == 31 || order.orderPayType == 1>
									（线下支付）
								<#else>
									（在线支付）
								</#if>
							</#if>
						<#else>
							&yen;${(order.depositePrice)!0}

						</#if>
						<#if order.refundAmount gt 0 >
							（已退款 ${order.refundAmount} 元）
						</#if>
					</span>
				</div>
			</#if>
		</div>

	<#if order.getCreatePointCount != 0>
		<div class="data-line">
			<span class="key">积分赠送：</span>
			<div>交易成功送<span class="theme2-color"> ${order.getCreatePointCount} </span>积分</div>
		</div>
	</#if>

		<div class="clear"></div>

	</div>

	<div class="u-title3">活动信息</div>
	<div class="order-data">
		<#if !((event.sourceProvince == "海外" || event.sourceProvince == "其他") && event.sourceDetailAddress == '')>
        <div class="data-line">
            <span class="key">集&ensp;合&ensp;地：</span>
            <div class="value">${formatAddress2(event,1)}</div>
        </div>
		</#if>
		<#if !((event.destProvince == "海外" || event.destProvince == "其他") && event.destDetailAddress == '')>
        <div class="data-line">
            <span class="key">目&ensp;的&ensp;地：</span>
            <div class="value">${formatAddress2(event,2)}</div>
        </div>
		</#if>
        <div class="data-line">
            <span class="key">${isHuwai?string("出发日期","开赛日期")}：</span>
            <div class="value">${formatDate(event.startTime, "yyyy-MM-dd")}</div>
        </div>
        <div class="data-line">
            <span class="key">结束日期：</span>
            <div class="value">${formatDate(event.endTime, 'yyyy-MM-dd')}</div>
        </div>
        <div class="data-line">
            <span class="key">${isHuwai?string("选择批次","选择分组")}：</span>
            <div class="value">${order.activityStyleClassTitle}</div>
        </div>
        <div class="data-line">
            <span class="key" id="sas-js-custom-modification-event">${isUserPrice?string('单　　价','会员价')}：</span>
            <div class="value theme2-color sas-js-custom-modification-event">¥${order.activityUnitPrice}</div>
        </div>
		<#if serviceTitles != ''>
            <div class="data-line2 clear">
                <span class="key">附加服务：</span>
                <div class="value">${serviceTitles}</div>
            </div>
		</#if>
	</div>
	<div class="u-title3">订单联系人<span></span></div>
	<div class="order-data">
		<div class="data-line">
			<div class="key">姓名：</div>
			<div class="value">${order.contactTrueName}</div>
		</div>
		<div class="data-line">
			<div class="key">手机号码：</div>
			<div class="value">${order.contactPhone}</div>
		</div>
	</div>
	<#if appliers?size gt 0>
	<div class="u-title3">报名人信息<span></span></div>
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

    <div class="u-title3">其他信息</div>
    <div class="other-field">

		<#if order.teamApplierInfoUrl != ''>
            <div class="field-line">
                <label for="">团队文件：</label>
				<a class="att" href="${order.teamApplierInfoUrl}" download="团队成员信息">
					<span class="fileicon fileicon-xls"></span>
					<span class="name c6"><#if currentSas.languageSupport == 'C'>团队成员信息.xls<#else>Team member information.xls</#if></span>
				</a>
            </div>
		</#if>
		<#if attList?size gt 0>
            <div class="field-line">
                <label for="">报名附件：</label>
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
            <label for="remark">订单备注：</label>
            <div class="remind">${(order.userRemark!="")?string(order.userRemark,'无')}</div>
        </div>
    </div>

	<#if (eventInfo.imGroupQRCode)?has_content>
        <div class="u-title3">活动微信群<small>（用微信扫描二维码加入群，实时获得通知）</small></div>
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


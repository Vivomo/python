<#-- @ftlvariable name="maxUsePointsMoney" type="java.lang.Number" -->
<#-- @ftlvariable name="lastOrder" type="com.sas.core.meta.SasMenuActivityOrder" -->
<#-- @ftlvariable name="captainTitle" type="java.lang.String" -->
<#-- @ftlvariable name="maxUsePoints" type="int" -->
<#-- @ftlvariable name="userGetPoints" type="int" -->
<#-- @ftlvariable name="imageList" type="java.util.List" -->
<#-- @ftlvariable name="detail" type="com.sas.core.dto.SasMenuActivityDetail" -->
<#include "inc/cfg.ftl">

<#global
assets_css = ['fileicons']
>

<#global
act = detail.activity
page_title = act.title
<#--U个人， T团队， A全部支持-->
applyType = act.applyMethodType
serviceList = detail.additionalServiceList![] <#--附加服务-->
styleClassList = detail.styleClassList <#--活动批次-->
attList = detail.attachmentList![]
appliers = detail.last10Appliers![]
page_name = "event"
page_css = ["event"]

<#--depositRatio = act.depositRatio 以前是比例 现在固定的-->
deposit = act.depositRatio
supportDeposit = deposit gte 0
>

<#assign isHuwai = sas_site_type == "huwai" />

<#include "inc/head.ftl">
<#escape x as x?html>
<body class="white">
<#include "inc/header.ftl">
	<#if menu_type == "ACTIVITY1">
		<@breadcrumb page_title/>
	<#else>
		<@breadcrumb />
	</#if>

<div class="act-detail u-box u-mode" data-id="${act.id}">
	<h2 class="act-title u-title">
		<span class="title-txt">${act.title}</span>
		<sub id="copy-link" class="f14 c9">[复制链接]</sub>
		<span class="user-data fr" style="position: relative;top:10px;"><#include "inc/jiathis.ftl"></span>
	</h2>

	<div class="img-wrap fl">
		<div class="big"><img src="${asset_image_blank}" data-src="${act.coverPicUrl}-w480h320"></div>
		<ul class="thumb-list">
		<#list imageList as img>
            <li class="theme-border-act <#if img_index == 0>active</#if>">
				<img src="${asset_image_blank}" data-src="${addImageURLQNSuffix(img, 'w300h200',asset_image_blank)}"
					 data-detail="${addImageURLQNSuffix(img, 'w480h320',asset_image_blank)}">
			</li>
		</#list>
		</ul>
	</div>
	<div class="data act-data-wrap">
		<#--已售出-->
		<div class="sold-out f13">
			已报名
			<span id="batchTotalApplier">${detail.statistic.totalApplierCount}</span> |
			余位 <span id="batchStoreCount">${act.storeCount}</span>
		</div>
		<div class="labelbackground">
		<#--售价-->
			<div class="label" id="sas-js-custom-modification-event">
				<span class="j-normal-price-field ">价格</span>
			</div>
			<div class="price theme2-color data-value sas-js-custom-modification-event">
				<span class="not-free price-for-user sas-js-custom-modification-line-height" style="vertical-align: super;">
					¥<strong class="price-num" id="normal-price">${styleClassList[0].price}</strong>
					<span class="f14"> / </span>
					<span class="f14 Micro">
						${act.priceUnitName}
							<span class="pay-line"> (支持线下支付)</span>
					</span>
				</span>
				<strong class="is-free f24 sas-js-is-free free-for-user">免费</strong>
			</div>
		<#--会员价-->
			<#if supportVip>
			<div class="label" id="sas-js-custom-modification-event">
				<span class="j-vip-price-field">会员价</span></div>
			<div class="price theme2-color data-value sas-js-custom-modification-event">
				<span class="not-free price-for-vip sas-js-custom-modification-line-height">
					¥<strong class="price-num" id="vip-price">${styleClassList[0].memberPrice}</strong>
					<span class="f14"> / </span>
					<span class="f14 Micro">
						${act.priceUnitName}
							<span class="pay-line"> (支持线下支付)</span>
					</span>
				</span>
				<strong class="is-free f24 sas-js-is-free free-for-vip">免费</strong>
			</div>
			</#if>
		</div>

		<#if userGetPoints + maxUsePoints != 0>

			<div class="label">积分详情</div>
			<div class="data-value giveIntegral">
				<#if userGetPoints gt 0>
                <div>
					<span class="title-integral">送积分</span>
					交易成功, 送${userGetPoints}积分
				</div>
				</#if>
				<#if maxUsePoints gt 0>
				<div>
					<span class="title-integral">抵现金</span>
					最多抵扣${maxUsePointsMoney!}元 (${maxUsePoints}积分)
				</div>
				</#if>
			</div>

		</#if>


		<div class="label"><span>${isHuwai?string("出发时间","开赛时间")}</span></div>
		<div class="start-time data-value">${formatDate(act.startTime, "yyyy-MM-dd HH:mm")}</div>
		<div class="label">${isHuwai?string("活动批次","比赛分组")}</div>
		<div class="data-value">
			<#if isHuwai>
				<div id="round-select">
					<div class="buttons batch-list">
						<#list detail.styleClassList as batch>
							<#assign isStyleAvailable = !batchCanSignUp(batch)>
							<button class="btn" ${isStyleAvailable?string('', 'disabled')}
							        data-start="${batch.startTime}"
							        data-id="${batch.id}" data-price="${batch.price}"
							        data-total-Applier-Count="${batch.totalApplierCount}"
							        data-store-Count="${batch.storeCount}"
                                    data-vip="${batch.memberPrice}"
							        data-line="${batch.payType}">
								<#if isStyleAvailable>
									<#if !firsteStyle??>
										<#assign firsteStyle = batch />
									</#if>
								</#if>
							${batch.title} （&yen; ${batch.price} / ${act.priceUnitName}）
							</button>
						</#list>
					</div>
					<#if !firsteStyle??>
						<#assign firsteStyle = detail.styleClassList[0]>
					</#if>
					<div class="caption btn" ${batchCanSignUp(firsteStyle)?string("disabled","")}>
						<div class="text text-ellipsis">
						${firsteStyle.title} （&yen; ${firsteStyle.price} / ${act.priceUnitName}）
						</div>
						<div class="arrowhead-down"></div>
					</div>
				</div>
			<#else>
				<ul class="batch-list">
					<#list styleClassList as batch>
						<li class="theme-border-act
				${ batchCanSignUp(batch)?string('disabled','')}"
						    data-start="${batch.startTime}"
						    data-id="${batch.id}" data-price="${batch.price}"
						    data-total-Applier-Count="${batch.totalApplierCount}"
						    data-store-Count="${batch.storeCount}"
                            data-vip="${batch.memberPrice}"
						    data-line="${batch.payType}">
						${batch.title}<i class="sp"></i><em class="theme-border r-b"></em>
						</li>
					</#list>
				</ul>
			</#if>
		</div>
		<#if serviceList?size gt 0>
			<div class="label">附加服务</div>
			<div class="data-value">
				<ul class="service-list">
					<#list serviceList as service>
						<li class="theme-border-act  ${ (service.storeCount lt 1)?string('disabled','')}"
						    data-id="${service.id}" data-price="${service.price}"
                            data-vip="${service.price}">
						${service.title}<i class="sp"></i><em class="theme-border r-b"></em>
						</li>
					</#list>
				</ul>
			</div>
		</#if>
		<#if supportDeposit>
            <div class="label">付款方式</div>
			<div class="data-value">
                <ul class="pay-type-list" id="pay-type-list">
                    <li class="theme-border-act active" data-type="N">
						全额付款<i class="sp"></i><em class="theme-border r-b"></em>
					</li>
                    <li class="theme-border-act" data-type="Y">
						预付定金<i class="sp"></i><em class="theme-border r-b"></em>
					</li>
                </ul>
			</div>
		</#if>
		<div class="dash-bottom"></div>
		<#if !((act.sourceProvince == "海外" || act.sourceProvince == "其他") && act.sourceDetailAddress == '')>
            <div class="label">
				<span>集&ensp;合&ensp;地</span>
			</div>
            <div class="data-value">${formatAddress2(act,1)}</div>
		</#if>
		<#if !((act.destProvince == "海外" || act.destProvince == "其他") && act.destDetailAddress == '')>
            <div class="label"><span>目&ensp;的&ensp;地</span></div>
            <div class="data-value">${formatAddress2(act,2)}</div>
		</#if>
		<#--<div class="label"><span>${isHuwai?string("出发时间","开赛时间")}</span></div>-->
		<#--<div class="start-time data-value">${formatDate(act.startTime, "yyyy-MM-dd HH:mm")}</div>-->
		<#if site_huwai && menu_type == "ACTIVITY1" && (detail.captain)?has_content>
			<div class="label"><span>${captainTitle}</span></div>
			<div class="data-value">
				${(detail.captain.nickName)!}　
				${(detail.captain.workPhone)!}
			</div>
		</#if>

		<#if site_huwai && (act.highlights)?has_content>
			<div class="label">活动亮点</div>
			<div class="data-value">
				${act.highlights}
			</div>
		</#if>
		<#if attList?size gt 0>
            <div class="label">附件下载</div>
			<div class="attachments data-value">
				<#list attList as att>
                 <a href="${att.url}" download="${att.name}" class="theme-border" target="_blank">
					 <i class="fileicon fileicon-${getFileExt(att.name)}"></i> ${att.name}
				 </a>
				</#list>
			</div>
		</#if>
		<#if lastOrder??>
		<div class="label">下单提醒</div>
        <div class="data-value">
            系统查询到您已报过名, <a href="/event/order?id=${lastOrder.orderCode}">直接付款 &gt;&gt;</a>
		</div>
		</#if>
		<div class="cols2 data-value">
			<#assign canSignUp = false>
			<#list styleClassList as batch>
				<#if batch.storeCount gte 1>
					<#assign canSignUp = true>
				</#if>
			</#list>

			<#if act.state == "F">
				<button class="join btn  disabled" disabled>活动已下架</button>
			<#elseif act.endTime?number_to_datetime lt .now>
				<button class="join btn  disabled" disabled>活动已结束</button>
			<#elseif act.applyExpireTime?number_to_datetime lt .now>
				<button class="join btn  disabled" disabled>报名已截止</button>
			<#elseif act.applyStartTime?number_to_datetime gt .now>
				<button class="join btn  theme2-bgcolor not-started">即将报名</button>
			<#elseif 0 gte act.storeCount || !canSignUp>
				<button class="join btn  disabled" disabled>报名人数已满</button>
			<#else>
				<#if act.foreignApplyURL == ''>
					<#if applyType != 'T'>
                        <button class="join  btn theme2-bgcolor ${userLogged?string('','anonymous')}"
							<#if !userLogged>useronly</#if>>我要报名</button>
					</#if>
					<#if applyType != 'U'>
                        <button class="join  btn theme-bgcolor team-join ${userLogged?string('','anonymous')}"
								data-type="T" <#if !userLogged>useronly</#if> >团队报名</button>
					</#if>
				<#else>
                    <a class="join theme2-bgcolor btn" href="${act.foreignApplyURL}" target="_blank">我要报名</a>
				</#if>
			</#if>
		</div>
	</div>

	<#if (act.remindNotice)?has_content>
        <div class="title-item clear">
            <span class="theme-bgcolor fl">注意事项</span><i class="theme-border left fl"></i>
        </div>
        <div class="act-detail content-box rich-text f14">
			<pre>${act.remindNotice}</pre>
        </div>
	</#if>

	<div class="title-item clear">
		<span class="theme-bgcolor fl">详细信息</span><i class="theme-border left fl"></i>
	</div>
	<div class="act-detail content-box rich-text">
		<#noescape>${act.content}</#noescape>
	</div>

	<#if attList?size gt 0>
		<div class="title-item">
			<span class="theme-bgcolor fl">附件列表</span><i class="theme-border left fl"></i>
		</div>
		<ul class="annex-list content-box">
			<#list attList as att>
				<li>
					<a href="${att.url}" download="${att.name}" class="theme-border" target="_blank">
						<i class="fileicon fileicon-${getFileExt(att.name)}"></i> ${att.name}
					</a>
				</li>
			</#list>
		</ul>
	</#if>
	<#if appliers?size gt 0>
	<div class="title-item">
		<span class="theme-bgcolor fl">最近报名</span><i class="theme-border left fl"></i>
	</div>
	<ul class="member-list content-box">
		<#list appliers as applier>
		<li><a href="user?id=${applier.id}">
				<img src="${applier.avatarUrl}" role="avatar">
				<div class="name ovl">${applier.nickname}</div>
			</a></li>
		</#list>
	</ul>
	</#if>


	<div id="reviewSection">
	<div class="title-item">
		<span class="theme-bgcolor fl">咨询留言</span><i class="theme-border left fl"></i>
	</div>
	<div class="content-box">
        <div class="empty-holder" id="comment-loading">正在加载留言数据...</div>
        <div id="error-msg"></div>
        <ul id="comment-list"></ul>
        <ul class="pagination" id="comment-paginator"></ul>
		<#if setting.activityCommentPubAuthority == "A" && act.commentPubAuthority == 'A'>
        <div class="x-media">
            <div class="media-left">
				<#if currentVisitor??>
                    <a href="${cfg_root_path}/user?id=${currentVisitor.id}"><img src="${currentVisitor.avatarUrl}" class="ava30" role="avatar"/></a>
				<#else>
                    <a href="javascript:;"><img src="${asset_avatar_default}" role="avatar" class="ava30"/></a>
				</#if>
            </div>
            <div class="media-main">
			<#if userLogged>
                <div>
                    <textarea class="u-editor" name="content" id="seditor" placeholder="说点什么吧~"></textarea>
                </div>
			<#else>
                <div class="u-editor">
                    评论请先<a href="javascript:;" useronly>登录</a>，或<a href="/register">注册</a>
                </div>
			</#if>
                <div class="media-footer">
                    <button class="btn btn-primary" ${userLogged?string("", "disabled")}
                            id="add-comment-btn">发布留言</button>
                    <span class="help-inline">Ctrl + Enter可以快速发布</span>
                </div>
            </div>
        </div>
		</#if>
	</div>
	</div>
</div>

<script>
    var eventId = ${(act.id)!0};
    var commentEnabled = ${(setting.activityCommentPubAuthority == "A" && act.commentPubAuthority == 'A')?c};
    var deposit = ${deposit};
</script>
<#include "inc/footer.ftl">
<#include "inc/scripts.ftl">
</#escape>
<script src="${cfg_assets_path}/js/fw/utilities/emojiutils.js?${cfg_version}"></script>
</body>
</html>

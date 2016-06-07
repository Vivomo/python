<#include "inc/cfg.ftl">

<#global
page_title = menu_name
page_name = "events"
page_css = ["events"]
>
<#assign mid = setting.menuId
		queryStr = '/events?mid='+mid
>
<#if categoryId!=-1>
	<#assign queryStr = '/events?mid='+mid+'&categoryId='+categoryId+'&timeCategoryId='+timeCategoryId+'&destAddressId='+destAddressId>
</#if>
<#if timeCategoryId!=-1>
	<#assign queryStr = '/events?mid='+mid+'&timeCategoryId='+timeCategoryId+'&destAddressId='+destAddressId+'&categoryId='+categoryId>
</#if>
<#if destAddressId!=-1>
	<#assign queryStr = '/events?mid='+mid+'&destAddressId='+destAddressId+'&categoryId='+categoryId+'&timeCategoryId='+timeCategoryId>
</#if>
<#if keyword!=''>
	<#assign queryStr = '/events/search?mid='+mid+'&keyword='+keyword>
</#if>


<#include "inc/head.ftl">
<body><#escape x as x?html>
<#include "inc/header.ftl">

<div class="container">
	<@breadcrumb />
    <div id="search-wrap">
        <form action="${cfg_root_path}/events/search" class="fr" id="search_form">
            <input type="hidden" name="mid" value="${mid}">
			<#if keyword != ''>
                <span>共搜到<span class="num theme2-color">${eventList?size}</span>个相关活动</span>
			</#if>
            <input autocomplete="off" type="text" name="keyword" value="${keyword!''}" id="keyword" placeholder="请输入关键词" required />
            <button class="submit sp" type="submit"></button>
        </form>
        <ul class="cookie-wrap"></ul>
    </div>
</div>
<@framework layout=sas_layout rightClass='events-container'>
	<div class="header">
		<div class="activity-wrap">
			<div class="act-classify">
			</div>
		</div>
		<#if categoryList??>
			<div class="classify-list">
				<div class="classify-name" data-key="${categoryId}">活动分类</div>
				<div class="list-wrap">
					<ul class="list">
						<li>
							<a href="${cfg_root_path +"/events?mid="+mid+'&destAddressId=${destAddressId}&timeCategoryId=${timeCategoryId}&categoryId=-1'}"
							   class="theme-bgcolor-act theme-border-act <#if categoryId==-1>active</#if>">全部</a>
						</li>
						<#list categoryList as item>
							<li>
								<a  class="theme-bgcolor-act theme-border-act <#if categoryId==item.id>active</#if>"
									data-id="${item.id}"
									href="${cfg_root_path}/events?mid=${mid}&destAddressId=${destAddressId}&timeCategoryId=${timeCategoryId}&categoryId=${item.id}">${item.name}</a>
							</li>
						</#list>
					</ul>
					<div class="more t-c">
						<a href="javascript:;" class="f12 sp">更多</a>
					</div>
				</div>
			</div>
		</#if>
		<#if destList?? && sas_site_type == "huwai">
			<div class="classify-list">
				<div class="classify-name" data-key="${destAddressId}">目的地</div>
				<div class="list-wrap">
					<ul class="list">
						<li>
							<a href="${cfg_root_path +"/events?mid="+mid+'&destAddressId=-1&timeCategoryId=${timeCategoryId}&categoryId=${categoryId}'}"
							   class="theme-bgcolor-act theme-border-act <#if destAddressId==-1>active</#if>">全部</a></li>
						<#list destList as d>
							<li>
								<a  class="theme-bgcolor-act theme-border-act <#if destAddressId==d.id>active</#if>"
									data-dest="${d.id}"
									href="${cfg_root_path}/events?mid=${mid}&destAddressId=${d.id}&timeCategoryId=${timeCategoryId}&categoryId=${categoryId}">${d.address}
								</a>
							</li>
						</#list>
					</ul>
					<div class="more t-c">
						<a href="javascript:;" class="f12 sp">更多</a>
					</div>
				</div>
			</div>
		</#if>
		<#if timeCategoryList??>
			<div class="classify-list">
				<div class="classify-name" data-key="${timeCategoryId}">活动时间</div>
				<div class="list-wrap">
					<ul class="list">
						<li>
							<a href="${cfg_root_path +"/events?mid="+mid+'&destAddressId=${destAddressId}&timeCategoryId=-1&categoryId=${categoryId}'}"
							   class="theme-bgcolor-act theme-border-act <#if timeCategoryId==-1>active</#if>">全部</a>
						</li>
						<#list timeCategoryList as item>
							<li><a  class="theme-bgcolor-act theme-border-act <#if timeCategoryId==item.id>active</#if>"
									data-id="${item.id}"
									data-name="${item.name}"
									href="${cfg_root_path}/events?mid=${mid}&destAddressId=${destAddressId}&categoryId=${categoryId}&timeCategoryId=${item.id}">
							${item.name}</a>
							</li>
						</#list>
					</ul>
					<div class="more t-c">
						<a href="javascript:;" class="f12 sp">更多</a>
					</div>
				</div>
			</div>
		</#if>


	</div>
	<div class="body">
		<#if setting.activityDisplayType == 'S'>
			<ul class="act2-list">
				<#list eventList as event>
					<#assign href = cfg_root_path+ "/event?id="+event.id+"&mid="+event.menuId>
					<li>
						<#if event.recommendState == 'R'>
							<a href="${href}" class="recommend sp">推荐</a>
						</#if>
						<div class="outline theme-outline-hov">
							<a target="_blank"  href="${href}" class="img-box">
								<img src="${asset_image_blank}" data-src="${event.coverPicUrl}-cw300h200" alt="${event.title}">
							</a>
							<a target="_blank"  href="${href}" class="title theme-color-hov ovl">${event.title}</a>
							<a target="_blank"  href="${href}" class="summary" <#if ((event.destProvince == "海外" || event.destProvince == "其他") && event.destDetailAddress == '')>style="height:96px;"</#if> >${event.content}</a>
							<div class="data f14">
								<div><span class="label">集合地：</span><span class="theme-color">${formatAddress(event, 1)} </span></div>
								<#if !((event.destProvince == "海外" || event.destProvince == "其他") && event.destDetailAddress == '')>
								<div><span class="label">目的地：</span><span class="theme-color">${formatAddress(event, 2)} </span></div>
								</#if>
								<div><span class="label">时　间：</span><span class="theme-color">${formatDate(event.startTime, "MM/dd")} - ${formatDate(event.endTime, "MM/dd")}</span></div>
							</div>
							<div class="price sas-js-words theme2-color sas-js-custom-modification-event">¥${event.priceMin} <span class="sas-js-word">${qi(event)}</span></div>
						</div>
					</li>
				</#list>
			</ul>
			<div id="paginator">
				<@pagination paginator=paginator query=queryStr/>
			</div>
		<#else>
			<div class="col4">
				<ul>
					<#list eventList as event>
						<#assign href = cfg_root_path+ "/event?id="+event.id+"&mid="+event.menuId>
						<li>
							<#if event.recommendState == 'R'>
								<a href="${href}" class="recommend sp">推荐</a>
							</#if>
							<a target="_blank" href="${href}" class="img-box">
								<img src="${asset_image_blank}" data-src="${event.coverPicUrl}-cw300h200">
							</a>
							<a target="_blank" href="${href}" class="title theme-color-hov c3" title="${event.title}">${event.title}</a>

							<div class="data-line ovl">集合地：<span class="theme-color">${formatAddress(event, 1)}</span></div>
							<div class="data-line ovl">时　间：<span class="theme-color">${formatDate(event.startTime, "MM/dd")} -
							${formatDate(event.endTime, "MM/dd")}</span></div>
							<div class="sas-js-custom-modification-event theme2-color data-line f18">¥${event.priceMin}<span class="sas-js-word f14"> ${qi(event)}</span></div>
						</li>
					</#list>
				</ul>
			</div>
			<div id="paginator">
				<@pagination paginator=paginator query=queryStr/>
			</div>
		</#if>

		<#if eventList?size == 0>
			<p class="f16 c9 t-c">对不起，没有搜索到对应的活动信息，试试
				<a href="${cfg_root_path +"/events?mid="+mid}" class="theme-color">查看全部</a> 哦！</p>
		</#if>

	</div>
</@framework>

<#include "inc/footer.ftl">
<#include "inc/scripts.ftl">
</#escape></body>
</html>

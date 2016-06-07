<#include "inc/cfg.ftl">

<#global
page_title = "报名条款"
page_name = "terms"
page_css = ["terms"]
>

<#include "inc/head.ftl">
<body><#escape x as x?html>
<#include "inc/header.ftl">
<div class="item-wrap u-box u-main">
    <h1 class="u-title t-c u-line">报名条款</h1>
    <div class="content f14"><#noescape >${applyRule}</#noescape></div>
    <#if eventStyleId??>
    <button class="submit theme-bgcolor2 f20" data-id="${eventInfo.id}" data-service="${serviceIds!''}"
			data-batch="${eventStyleId}">我同意报名条款并报名</button>
    </#if>
</div>
<#include "inc/footer.ftl">
<#include "inc/scripts.ftl">
</#escape></body>
</html>

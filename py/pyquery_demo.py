from pyquery import PyQuery as pq

from lxml import etree

html = '''
<div class="data" style="height:auto;">
            <i class="icon icon-paperclip"></i>
			<span class="label">附件下载</span>
			<ul class="attachmentList value">
                <#list detail.attachmentList as atta>
					<li>
						<a href="${atta.url}" download="${atta.name}" target="_blank">
							<i class="fileicon fileicon-lg fileicon-${getFileExt(atta.name)}"></i> ${atta.name}
						</a>
					</li>
                </#list>
			</ul>
		</div>
	</div>
'''

d = pq(html)
nullNode = d.find('.label').children().length
print(nullNode)

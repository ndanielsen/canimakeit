

class FakeBadResponse(object):
    status_code = 404
    url = 'dummy url'


html = '''
<div>
    <a href = "link 1">link 1</a>
    <a href = "link 2">link 2</a>
    <img src = "not a link"></img>
    <div class="nested">
        <a href = "link 3">link 3</a>
    </div>
</div>
'''

links = ['link 1', 'link 2', 'link 3']

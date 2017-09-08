class HtmlOutPuter(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    #ascii
    def output_html_old(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' %data['url'].encode('utf-8'))
            fout.write('<td>%s</td>' %data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' %data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')


    def output_html(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write('<body>')

        for data in self.datas:
            fout.write('<p>')
            fout.write('<h2> %s</h2>' %data['title'].encode('utf-8'))
            #fout.write('url:%s\n' %data['url'].encode('utf-8'))
            fout.write('%s\n' %data['summary'].encode('utf-8'))
            fout.write('</p>')

        fout.write('</body>')
        fout.write('</html>')



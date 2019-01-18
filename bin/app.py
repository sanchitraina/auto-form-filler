import web

urls = (
	'/hello', 'Index',
	'/upload', 'Upload'
	)

app = web.application(urls, globals())
message = ''
render = web.template.render('templates/', base="layout")

class Index(object):

	def GET(self):
		return render.hello_form_laid_out()

	def POST(self):
		form = web.input(name = "Nobody", greet = "Hello")
		greeting = "%s %s" % (form.greet, form.name)
		return render.index_laid_out(greeting = greeting)

class Upload(object):

	def GET(self):
		return render.upload_laid_out(message = message)

	def POST(self):
		file_org = web.input(myfile={})
		if file_org:
			message = "file is stored"
		else:
			message = "failure"
		return render.upload_laid_out(message = message)

if __name__ == "__main__":
	app.run()
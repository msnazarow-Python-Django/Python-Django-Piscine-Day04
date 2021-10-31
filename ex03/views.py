from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
	template_name = 'ex03/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['colors'] = [{
			'black': f'#{i:02x}{i:02x}{i:02x}',
			'blue': f'#0000{i:02x}',
			'green': f'#00{i:02x}00',
			'red': f'#{i:02x}0000'
		} for i in range(0xFF, 5, -(0xFF // 50))]
		context['range'] = range(50)
		return context

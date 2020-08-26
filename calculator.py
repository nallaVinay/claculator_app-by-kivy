from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import math
import cmath


class CalcWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, '.', 0, '%']
        symbols1 = ['-', '(', 'AC', ')', '\u00f7', 'mod', '\u00d7\u00b2', '\u03c0', '\u221a']
        symbols = ['C', '\u00d7', '+']
        self.text = ''
        self.butt = self.ids.number
        self.butt1 = self.ids.numbers
        self.symb = self.ids.sym
        for i in numbers:
            but = Button(text=str(i), background_normal='', background_color=(0.004, 0.055, 0.102, 1.0))
            but.bind(on_release=self.echo_num)
            self.butt.add_widget(but)

        for i in symbols1:
            but = Button(text=str(i), background_normal='', background_color=(0.004, 0.055, 0.102, 1.0))
            but.bind(on_release=self.echo_num)
            self.butt1.add_widget(but)
        b = Button(text='=', background_normal='', background_color=(0.133, 0.855, 0.431, 1.0))
        b.bind(on_release=self.evaluation)
        self.ids.box1.add_widget(b)
        for i in symbols:
            if i == '+':
                but = Button(text=str(i), size_hint_y=.40, background_normal='',
                             background_color=(0.004, 0.055, 0.102, 1.0))
                but.bind(on_release=self.echo_num)
            else:
                but = Button(text=str(i), size_hint_y=.30, background_normal='',
                             background_color=(0.004, 0.055, 0.102, 1.0))
                but.bind(on_release=self.echo_num)
            self.symb.add_widget(but)

    def echo_num(self, instance):
        query = self.ids.binding
        if instance.text == '%' and len(query.text) > 0:
            sym = []
            sym.append(query.text.rfind('-'))
            sym.append(query.text.rfind('+'))
            sym.append(query.text.rfind('\u00f7'))
            sym.append(query.text.rfind('\u00d7'))
            sym_ind = max(sym)
            if sym_ind < 0:
                prec = round(float(query.text) / 100, 2)
                query.text = str(prec)
            else:
                res = query.text
                target = res[sym_ind + 1:]
                prec = round(float(target) / 100, 2)
                query.text = str(prec)
        elif instance.text == '\u221a' and len(query.text) > 0:
            sym = [query.text.rfind('-'), query.text.rfind('+'), query.text.rfind('\u00f7'), query.text.rfind('\u00d7')]
            sym_ind = max(sym)
            if sym_ind < 0:
                squ = math.sqrt(float(query.text))
                query.text = str(squ)
            else:
                res = query.text
                target = res[sym_ind + 1:]
                squ = math.sqrt(float(target))
                query.text = str(squ)
        elif instance.text == 'AC':
            self.ids.binding.text = ''
            self.ids.text_q.text = ''
            self.ids.equal.text = ''
        elif instance.text == 'C':
            self.ids.binding.text = query.text[:-1]

        else:
            query.text += instance.text

    def evaluation(self, text):
        try:
           
            query = self.ids.binding
            exp = query.text
            if exp =='mod143':
                self.ids.binding.text = 'I LOVE YOU AMMA,😘😘😘😘'
            else:
               exp = self.resolve(exp)
               res = eval(exp)
               query.text = str(res)
               self.ids.text_q.text = str(exp) + '='
               self.ids.equal.text = str(res)
        except:
            self.ids.binding.text = 'please enter a valid syntax\nNOTE: please use \u221a symbol after number'

    def resolve(self, text):
        res = text.replace('\u00f7', '/').replace('\u00d7\u00b2', '**2').replace('\u00d7', '*').replace('\u03c0',
                                                                                                        str(cmath.pi))
        return res


class CalcApp(App):
    def build(self):
        return CalcWindow()


if __name__ == '__main__':
    CalcApp().run()

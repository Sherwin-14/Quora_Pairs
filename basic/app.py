from shiny import reactive
from shiny.express import expressify, input, render, ui, output, session
import helper
import pickle

model = pickle.load(open('xgb_model.pkl','rb'))

ui.tags.style(
  """

   .yes {
  text-align: center;
  font-size: 24px; /* adjust the font size as needed */
  }

   .no {
    text-align: center;
    font-size: 24px; /* adjust the font size as needed */
    }


""")

ui.page_opts(title="Quora Challenge - Are These Two Questions The Same?", fillable=True)

with ui.card():
    ui.card_header("Type two questions and check wether these two questions are of similar mould")
    ui.br(_add_ws=True)
    ui.input_text_area("caption1", "Question 1:", "Enter Question 1",width='100%',height='100%')
    ui.br(_add_ws=True)
    ui.br(_add_ws=True)
    ui.br(_add_ws=True)
    ui.input_text_area("caption2", "Question 2:", "Enter Question 2",width='100%',height='100%') 
    ui.br(_add_ws=True)
    ui.br(_add_ws=True)
    ui.br(_add_ws=True)
    ui.input_action_button(id="btn",label="Find",width='10%',)

    ui.card_footer("The Model has an accuracy near about 80%")

with ui.sidebar(class_="mt-1"):
    ui.h4("Result Pane ")
    @render.text()
    @reactive.event(input.btn)
    def display():
        query = helper.query_point_creator(input.caption1(),input.caption2())
        result = model.predict(query)[0]

        if result:
            return "Yes"
        else:
            return "No"   
     







          
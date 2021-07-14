import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

gpt.add_example(Example("What is AA amyloidosis?", "Secondary amyloidosis is a form of amyloidosis (see this term), that complicates chronic inflammatory disorders (mainly rheumatoid arthritis, see this term) and is characterized by the aggregation and deposition of amyloid fibrils composed of serum amyloid A protein, an acute phase reactant. Although spleen, suprarenal gland, liver and gut are frequent sites of amyloid deposition, the clinical picture is dominated by renal involvement."))
gpt.add_example(Example("What is AAA syndrome?", "Triple A syndrome is a very rare multisystem disease characterized by adrenal insufficiency with isolated glucocorticoid deficiency, achalasia, alacrima, autonomic dysfunction and neurodegeneration."))

# Define UI configuration
config = UIConfig(
    description="Prompt",
    button_text="Result",
    placeholder="What is AADC deficiency?",
    show_example_form=True,
)

demo_web_app(gpt, config)
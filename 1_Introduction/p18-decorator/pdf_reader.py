import nest_asyncio
import os

from llama_parse import LlamaParse
from llama_index.core.node_parser import MarkdownElementNodeParser

nest_asyncio.apply()


os.environ["LLAMA_CLOUD_API_KEY"] = "llx-vEIZ44OsMv51b5Ldd10EgsOVmyY8f7dtMSVvvab7nEaAqHrY"


parser = LlamaParse(
    result_type="text",
    language="ch_sim",
    verbose=True,
    num_workers=1,
)

documents = parser.load_data("CN111709349B.pdf")

for document in documents:
    # print(document.text)
    print(document.get_content())


node_parser = MarkdownElementNodeParser(llm=OpenAI(model="gpt-3.5-turbo-16k"), num_workers=2)
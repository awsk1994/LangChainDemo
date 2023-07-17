from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

information = """
Elon Reeve Musk is a business magnate and investor. 
"""

if __name__ == "__main__":
    print("Hello Langchain")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    llm = LlamaCpp(
        model_path="./ggml-model-q4_0.bin",
        callback_manager=callback_manager,
        verbose=True,
    )
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(information=information))

from typing import Dict, Callable, List
from langchain.base_language import BaseLanguageModel
from langchain.tools.base import BaseTool
from langchain.agents import load_tools, get_all_tool_names

from chatmof.tools.predictor import _get_predict_properties
from chatmof.tools.search_csv import _get_search_csv
from chatmof.tools.genetic_algorithm import _get_generator


_MOF_TOOLS: Dict[str, Callable[[BaseLanguageModel], BaseTool]] = {
    "search_csv" : _get_search_csv,
    "predictor": _get_predict_properties,
    'generator': _get_generator,
}

_load_tool_names: List[str] = [
    #'python_repl',
    #'requests',
    #'requests_get',
    #'requests_post',
    #'requests_patch',
    #'requests_put',
    #'requests_delete',
    #'terminal',
    'google-search',
    'google-search-results-json',
    'wikipedia',
    'human',
    'llm-math',
    'pal-math'
]


def load_chatmof_tools(llm: BaseLanguageModel, verbose: bool=False) -> List[BaseTool]:
    tools = load_tools(_load_tool_names, llm=llm)
    custom_tools = [model(llm=llm, verbose=verbose) for model in _MOF_TOOLS.values()]
    return custom_tools + tools
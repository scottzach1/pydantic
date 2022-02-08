import warnings

from pydantic import BaseModel, Extra

warnings.filterwarnings('error')


class FooBarModel(BaseModel):
    a: str

    class Config:
        extra = Extra.allow  # also supports `Extra.ignore`
        extra_warn = True


try:
    FooBarModel(a='hello', b=0.5)
except RuntimeWarning as w:
    print(w)

# Text Sentiment Analysis Example

This example uses the [HuggingFace DistilBERT base uncased finetuned SST-2](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) AI model to perform text sentiment analysis. The Caikit runtime loads the model and serves it so that it can be inferred or called.

## Before Starting

The following tools are required:

- [python](https://www.python.org) (v3.8+)
- [pip](https://pypi.org/project/pip/) (v23.0+)

**Note: Before installing dependencies and to avoid conflicts in your environment, it is advisable to use a [virtual environment(venv)](https://docs.python.org/3/library/venv.html).**

Install the dependencies: 

```sh
cd examples/text-sentiment
python3.11 -m venv caikit-env-3.11
source ./caikit-env-3.11/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

## Start the `Caikit runtime server`

Start the `Caikit runtime server` in the first terminal: 

```shell
cd examples/text-sentiment
source ./caikit-env-3.11/bin/activate
python3 start_runtime.py
```

* Example output:

```sh
<function register_backend_type at 0x7fce0064b5e0> is still in the BETA phase and subject to change!
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: text_sentiment", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.808812"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.common", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.809406"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.runtime", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.809565"}
[…]
{"channel": "MODEL-LOADER", "exception": null, "level": "info", "log_code": "<RUN89711114I>", "message": "Loading model 'text_sentiment'", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.826657"}
{"channel": "MDLMNG", "exception": null, "level": "warning", "log_code": "<COR56759744W>", "message": "No backend configured! Trying to configure using default config file.", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.827742"}
No model was supplied, defaulted to distilbert-base-uncased-finetuned-sst-2-english and revision af0f99b (https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
[…]
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: text_sentiment", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929756"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.common", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929814"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.runtime", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929858"}
{"channel": "GP-SERVICR-I", "exception": null, "level": "info", "log_code": "<RUN76773778I>", "message": "Validated Caikit Library CDM successfully", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929942"}
{"channel": "GP-SERVICR-I", "exception": null, "level": "info", "log_code": "<RUN76884779I>", "message": "Constructed inference service for library: text_sentiment, version: unknown", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.930734"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN81194024I>", "message": "Intercepting RPC method /caikit.runtime.HfTextsentiment.HfTextsentimentService/HfBlockPredict", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.930786"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN33333123I>", "message": "Wrapping safe rpc for Predict", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.931424"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN30032825I>", "message": "Re-routing RPC /caikit.runtime.HfTextsentiment.HfTextsentimentService/HfBlockPredict from <function _ServiceBuilder._GenerateNonImplementedMethod.<locals>.<lambda> at 0x7fce01f660d0> to <function CaikitRuntimeServerWrapper.safe_rpc_wrapper.<locals>.safe_rpc_call at 0x7fce02144670>", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.931479"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN24924908I>", "message": "Interception of service caikit.runtime.HfTextsentiment.HfTextsentimentService complete", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.931530"}
[…]

{"channel": "GRPC-SERVR", "exception": null, "level": "info", "log_code": "<RUN10001807I>", "message": "Running in insecure mode", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.936511"}
{"channel": "GRPC-SERVR", "exception": null, "level": "info", "log_code": "<RUN10001001I>", "message": "Caikit Runtime is serving on port: 8085 with thread pool size: 5", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.938054"}
```

## Start the `Caikit client` to infer the served model

Start the `Caikit client` in the second terminal:

```shell
cd examples/text-sentiment
source ./caikit-env-3.11/bin/activate
python3 client.py
```

The client code calls the model and queries it for sentiment analysis on 2 different pieces of text.

* Example output:

```sh
<function register_backend_type at 0x10d994040> is still in the BETA phase and subject to change!

*** 
 Client stub:
--
 <py_to_proto.json_to_service.TextSentimentServiceStub object at 0x10c82cb90>
--


*** 
 Verify if the with grpc command is available:
--
 ['HfModulePredict', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
--

Input text proto: 'text: "I am not feeling well today!"
'
Text: I am not feeling well today!
RESPONSE: classes {
  class_name: "NEGATIVE"
  confidence: 0.99977594614028931
}

Input text proto: 'text: "Today is a nice sunny day"
'
Text: Today is a nice sunny day
RESPONSE: classes {
  class_name: "POSITIVE"
  confidence: 0.999869704246521
}
```

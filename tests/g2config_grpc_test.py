import json

import grpc
import pytest
from pytest_schema import Or, schema
from senzing_abstract import g2exception

from senzing_grpc import G2BadInputError, g2config_grpc

# -----------------------------------------------------------------------------
# G2Config testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, g2config_grpc.G2ConfigGrpc)


def test_add_data_source(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().add_data_source()."""
    input_json_dict = {"DSRC_CODE": "NAME_OF_DATASOURCE"}
    config_handle = g2_config.create()
    actual = g2_config.add_data_source(config_handle, json.dumps(input_json_dict))
    g2_config.close(config_handle)
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(add_data_source_schema) == actual_json


def test_add_data_source_dict(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().add_data_source()."""
    input_json_dict = {"DSRC_CODE": "NAME_OF_DATASOURCE"}
    config_handle = g2_config.create()
    actual = g2_config.add_data_source(config_handle, input_json_dict)
    g2_config.close(config_handle)
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(add_data_source_schema) == actual_json


def test_add_data_source_bad_config_handle_type(
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Config().add_data_source()."""
    bad_config_handle = "string"
    input_json_dict = {"DSRC_CODE": "NAME_OF_DATASOURCE"}
    with pytest.raises(TypeError):
        g2_config.add_data_source(
            bad_config_handle, json.dumps(input_json_dict)  # type: ignore[arg-type]
        )


# TODO: Crashes the gRPC Server.
# def test_add_data_source_bad_config_handle_value(g2_config: g2config_grpc.G2ConfigGrpc):
#     """Test G2Config().add_data_source()."""
#     bad_config_handle = 1234
#     input_json_dict = {"DSRC_CODE": "NAME_OF_DATASOURCE"}
#     with pytest.raises(TypeError):
#         g2_config.add_data_source(bad_config_handle, json.dumps(input_json_dict))


def test_add_data_source_bad_input_json_type(
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Config().add_data_source()."""
    config_handle = g2_config.create()
    bad_input_json = 0
    try:
        with pytest.raises(TypeError):
            g2_config.add_data_source(
                config_handle, bad_input_json  # type: ignore[arg-type]
            )
    finally:
        g2_config.close(config_handle)


def test_add_data_source_bad_input_json_value(
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Config().add_data_source()."""
    config_handle = g2_config.create()
    bad_input_dict = {"XXXX": "YYYY"}
    try:
        with pytest.raises(G2BadInputError):
            g2_config.add_data_source(config_handle, bad_input_dict)
    finally:
        g2_config.close(config_handle)


def test_close_bad_config_handle_type(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().create()."""
    bad_config_handle = "string"
    with pytest.raises(TypeError):
        g2_config.close(bad_config_handle)  # type: ignore[arg-type]


# TODO: Crashes the gRPC Server.
# def test_close_bad_config_handle_value(g2_config: g2config_grpc.G2ConfigGrpc):
#     """Test G2Config().create()."""
#     bad_config_handle = 1234
#     with pytest.raises(TypeError):
#         g2_config.close(bad_config_handle)


def test_create(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().create()."""
    config_handle = g2_config.create()
    assert isinstance(config_handle, int)
    assert config_handle > 0
    g2_config.close(config_handle)
    assert isinstance(config_handle, int)
    assert config_handle > 0


def test_delete_data_source(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().delete_data_source()."""
    input_json_dict = {"DSRC_CODE": "TEST"}
    config_handle = g2_config.create()
    g2_config.delete_data_source(config_handle, json.dumps(input_json_dict))
    g2_config.close(config_handle)


def test_delete_data_source_dict(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().delete_data_source()."""
    input_json_dict = {"DSRC_CODE": "TEST"}
    config_handle = g2_config.create()
    g2_config.delete_data_source(config_handle, input_json_dict)
    g2_config.close(config_handle)


def test_delete_data_source_bad_config_handle_type(
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Config().delete_data_source()."""
    input_json_dict = {"DSRC_CODE": "TEST"}
    bad_config_handle = "string"
    with pytest.raises(TypeError):
        g2_config.delete_data_source(
            bad_config_handle, json.dumps(input_json_dict)  # type: ignore[arg-type]
        )


# TODO: Crashes the gRPC Server.
# def test_delete_data_source_bad_config_handle_value(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
#     """Test G2Config().delete_data_source()."""
#     input_json_dict = {"XXXX": "YYYY"}
#     config_handle = 1234
#     g2_config.delete_data_source(config_handle, json.dumps(input_json_dict))
#     g2_config.close(config_handle)


def test_delete_data_source_bad_input_json_type(
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Config().delete_data_source()."""
    bad_input_json = 0
    config_handle = g2_config.create()
    with pytest.raises(TypeError):
        g2_config.delete_data_source(
            config_handle, bad_input_json  # type: ignore[arg-type]
        )
    g2_config.close(config_handle)


def test_delete_data_source_bad_input_json_value(
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Config().delete_data_source()."""
    input_json_dict = {"XXXX": "YYYY"}
    config_handle = g2_config.create()
    g2_config.delete_data_source(config_handle, json.dumps(input_json_dict))
    g2_config.close(config_handle)


def test_list_data_sources(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().list_data_sources()."""
    config_handle = g2_config.create()
    actual = g2_config.list_data_sources(config_handle)
    g2_config.close(config_handle)
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(list_data_sources_schema) == actual_json


def test_list_data_sources_bad_config_handle_type(
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Config().list_data_sources()."""
    bad_config_handle = "string"
    with pytest.raises(TypeError):
        g2_config.list_data_sources(bad_config_handle)  # type: ignore[arg-type]


# TODO: Crashes the gRPC Server.
# def test_list_data_sources_bad_config_handle_value(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
#     """Test G2Config().list_data_sources()."""
#     bad_config_handle = 1
#     with pytest.raises(TypeError):
#         g2_config.list_data_sources(bad_config_handle)


def test_load(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().load()."""
    config_handle = g2_config.create()
    json_config = g2_config.save(config_handle)
    config_handle = g2_config.load(json_config)
    assert isinstance(config_handle, int)
    assert config_handle > 0
    g2_config.close(config_handle)


def test_load_dict(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().load()."""
    config_handle = g2_config.create()
    json_config = g2_config.save(config_handle)
    json_config_dict = json.loads(json_config)
    config_handle = g2_config.load(json_config_dict)
    assert isinstance(config_handle, int)
    assert config_handle > 0
    g2_config.close(config_handle)


def test_load_bad_json_config_type(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().load()."""
    bad_json_config = 0
    with pytest.raises(TypeError):
        g2_config.load(bad_json_config)  # type: ignore[arg-type]


def test_load_bad_json_config_value(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().load()."""
    bad_json_config = {"Just": "Junk"}
    with pytest.raises(g2exception.G2ConfigurationError):
        g2_config.load(bad_json_config)


def test_save(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().save()."""
    config_handle = g2_config.create()
    actual = g2_config.save(config_handle)
    g2_config.close(config_handle)
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(save_schema) == actual_json


def test_save_bad_config_handle_type(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().save()."""
    bad_config_handle = "string"
    with pytest.raises(TypeError):
        g2_config.save(bad_config_handle)  # type: ignore[arg-type]


# TODO: Crashes the gRPC Server.
# def test_save_bad_config_handle_value(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
#     """Test G2Config().save()."""
#     bad_config_handle = 1234
#     with pytest.raises(TypeError):
#         g2_config.save(bad_config_handle)


def test_init_and_destroy(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().init() and G2Config.destroy()."""
    g2_config.init("Example", "{}", 0)
    g2_config.destroy()


def test_init_and_destroy_dict(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().init() and G2Config.destroy()."""
    g2_config.init("Example", {}, 0)
    g2_config.destroy()


def test_init_and_destroy_again(g2_config: g2config_grpc.G2ConfigGrpc) -> None:
    """Test G2Config().init() and G2Config.destroy()."""
    g2_config.init("Example", "{}", 0)
    g2_config.destroy()


def test_context_managment() -> None:
    """Test the use of G2ConfigGrpc in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel) as g2_config:
        config_handle = g2_config.create()
        actual = g2_config.list_data_sources(config_handle)
        g2_config.close(config_handle)
        assert isinstance(actual, str)
        actual_json = json.loads(actual)
        assert schema(list_data_sources_schema) == actual_json


# -----------------------------------------------------------------------------
# G2Config fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_config", scope="module")  # type: ignore[misc]
def g2config_fixture() -> g2config_grpc.G2ConfigGrpc:
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    return result


# -----------------------------------------------------------------------------
# G2Config schemas
# -----------------------------------------------------------------------------

add_data_source_schema = {
    "DSRC_ID": int,
}

list_data_sources_schema = {
    "DATA_SOURCES": [
        {
            "DSRC_ID": int,
            "DSRC_CODE": str,
        },
    ]
}

save_schema = {
    "G2_CONFIG": {
        "CFG_ATTR": [
            {
                "ATTR_ID": int,
                "ATTR_CODE": str,
                "ATTR_CLASS": str,
                "FTYPE_CODE": Or(str, None),
                "FELEM_CODE": Or(str, None),
                "FELEM_REQ": str,
                "DEFAULT_VALUE": Or(str, None),
                "ADVANCED": str,
                "INTERNAL": str,
            },
        ],
        "CFG_CFBOM": [
            {
                "CFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_CFCALL": [
            {
                "CFCALL_ID": int,
                "FTYPE_ID": int,
                "CFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_CFRTN": [
            {
                "CFRTN_ID": int,
                "CFUNC_ID": int,
                "FTYPE_ID": int,
                "CFUNC_RTNVAL": str,
                "EXEC_ORDER": int,
                "SAME_SCORE": int,
                "CLOSE_SCORE": int,
                "LIKELY_SCORE": int,
                "PLAUSIBLE_SCORE": int,
                "UN_LIKELY_SCORE": int,
            },
        ],
        "CFG_CFUNC": [
            {
                "CFUNC_ID": int,
                "CFUNC_CODE": str,
                "CFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "ANON_SUPPORT": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_DFBOM": [
            {
                "DFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_DFCALL": [
            {
                "DFCALL_ID": int,
                "FTYPE_ID": int,
                "DFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_DFUNC": [
            {
                "DFUNC_ID": int,
                "DFUNC_CODE": str,
                "DFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "ANON_SUPPORT": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_DSRC": [
            {
                "DSRC_ID": int,
                "DSRC_CODE": str,
                "DSRC_DESC": str,
                "DSRC_RELY": int,
                "RETENTION_LEVEL": str,
                "CONVERSATIONAL": str,
            },
        ],
        "CFG_DSRC_INTEREST": [],
        "CFG_ECLASS": [
            {
                "ECLASS_ID": int,
                "ECLASS_CODE": str,
                "ECLASS_DESC": str,
                "RESOLVE": str,
            },
        ],
        "CFG_EFBOM": [
            {
                "EFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
                "FELEM_REQ": str,
            },
        ],
        "CFG_EFCALL": [
            {
                "EFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EFUNC_ID": int,
                "EXEC_ORDER": int,
                "EFEAT_FTYPE_ID": int,
                "IS_VIRTUAL": str,
            },
        ],
        "CFG_EFUNC": [
            {
                "EFUNC_ID": int,
                "EFUNC_CODE": str,
                "EFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_ERFRAG": [
            {
                "ERFRAG_ID": int,
                "ERFRAG_CODE": str,
                "ERFRAG_DESC": str,
                "ERFRAG_SOURCE": str,
                "ERFRAG_DEPENDS": Or(str, None),
            },
        ],
        "CFG_ERRULE": [
            {
                "ERRULE_ID": int,
                "ERRULE_CODE": str,
                "ERRULE_DESC": str,
                "RESOLVE": str,
                "RELATE": str,
                "REF_SCORE": int,
                "RTYPE_ID": int,
                "QUAL_ERFRAG_CODE": str,
                "DISQ_ERFRAG_CODE": Or(str, None),
                "ERRULE_TIER": Or(int, None),
            },
        ],
        "CFG_ETYPE": [
            {
                "ETYPE_ID": int,
                "ETYPE_CODE": str,
                "ETYPE_DESC": str,
                "ECLASS_ID": int,
            },
        ],
        "CFG_FBOM": [
            {
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
                "DISPLAY_LEVEL": int,
                "DISPLAY_DELIM": Or(str, None),
                "DERIVED": str,
            },
        ],
        "CFG_FBOVR": [
            {
                "FTYPE_ID": int,
                "ECLASS_ID": int,
                "UTYPE_CODE": str,
                "FTYPE_FREQ": str,
                "FTYPE_EXCL": str,
                "FTYPE_STAB": str,
            },
        ],
        "CFG_FCLASS": [
            {
                "FCLASS_ID": int,
                "FCLASS_CODE": str,
                "FCLASS_DESC": str,
            },
        ],
        "CFG_FELEM": [
            {
                "FELEM_ID": int,
                "FELEM_CODE": str,
                "FELEM_DESC": str,
                "TOKENIZE": str,
                "DATA_TYPE": str,
            },
        ],
        "CFG_FTYPE": [
            {
                "FTYPE_ID": int,
                "FTYPE_CODE": Or(str, None),
                "FTYPE_DESC": str,
                "FCLASS_ID": int,
                "FTYPE_FREQ": str,
                "FTYPE_EXCL": str,
                "FTYPE_STAB": str,
                "PERSIST_HISTORY": str,
                "USED_FOR_CAND": str,
                "DERIVED": str,
                "DERIVATION": Or(str, None),
                "RTYPE_ID": int,
                "ANONYMIZE": str,
                "VERSION": int,
                "SHOW_IN_MATCH_KEY": str,
            },
        ],
        "CFG_GENERIC_THRESHOLD": [
            {
                "GPLAN_ID": int,
                "BEHAVIOR": str,
                "FTYPE_ID": int,
                "CANDIDATE_CAP": int,
                "SCORING_CAP": int,
                "SEND_TO_REDO": str,
            },
        ],
        "CFG_GPLAN": [
            {
                "GPLAN_ID": int,
                "GPLAN_CODE": str,
                "GPLAN_DESC": str,
            },
        ],
        "CFG_LENS": [
            {
                "LENS_ID": int,
                "LENS_CODE": str,
                "LENS_DESC": str,
            },
        ],
        "CFG_LENSRL": [],
        "CFG_RCLASS": [
            {
                "RCLASS_ID": int,
                "RCLASS_CODE": str,
                "RCLASS_DESC": str,
                "IS_DISCLOSED": str,
            },
        ],
        "CFG_RTYPE": [
            {
                "RTYPE_ID": int,
                "RTYPE_CODE": str,
                "RTYPE_DESC": str,
                "RCLASS_ID": int,
                "REL_STRENGTH": int,
                "BREAK_RES": str,
            },
        ],
        "CFG_SFCALL": [
            {
                "SFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "SFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_SFUNC": [
            {
                "SFUNC_ID": int,
                "SFUNC_CODE": str,
                "SFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "SYS_OOM": [
            {
                "OOM_TYPE": str,
                "OOM_LEVEL": str,
                "LENS_ID": int,
                "FTYPE_ID": int,
                "LIB_FEAT_ID": int,
                "FELEM_ID": int,
                "LIB_FELEM_ID": int,
                "THRESH1_CNT": int,
                "THRESH1_OOM": int,
                "NEXT_THRESH": int,
            },
        ],
        "CONFIG_BASE_VERSION": {
            "VERSION": str,
            "BUILD_VERSION": str,
            "BUILD_DATE": str,
            "BUILD_NUMBER": str,
            "COMPATIBILITY_VERSION": {
                "CONFIG_VERSION": str,
            },
        },
    },
}

from typing import Union, Tuple
from datetime import datetime
import json
from g2_flags import *

class G2EngineClient:
    def __init__(self):
        self.type = None
        self.connector = None

    #internal methods
    def __init_grpc_connector(self) -> None:
        import g2_engine_grpc_connector
        self.type = 'GRPC'
        self.connector = g2_engine_grpc_connector.G2EngineGRPCConnector()


    def __init_direct_connector(self) -> None:
        import g2_engine_direct_connector
        self.type = 'DIRECT'
        self.connector = g2_engine_direct_connector.G2EngineDirectConnector()

    #startup/shutdown methods
    def init_grpc_connection_with_url(self, url: str) -> None:
        self.__init_grpc_connector()
        self.connector.init_with_url(url)

    def init_direct(self,
                    module_name: str,
                    senzing_config_json: Union[str,dict], 
                    config_id: int=None,
                    verbose_logging: bool=False) -> None:
        self.__init_direct_connector()
        if isinstance(ini_params, dict):
            ini_params = json.dumps(ini_params)

        self.connector.init_direct(
            module_name=module_name,
            senzing_config_json=senzing_config_json,
            config_id=config_id,
            verbose_logging=verbose_logging)

    def init_direct_from_environment(self,
                                     module_name: str,
                                     config_id: int=None,
                                     verbose_logging: bool=False) -> None:
        self.__init_direct_connector()
        return self.connector.init_direct_from_environment(
            module_name=module_name,
            config_id=config_id,
            verbose_logging=verbose_logging
            )

    def reinit(self, config_id: int) -> None:
        config_id = int(config_id)
        self.connector.reinit(config_id=config_id)

    def destroy(self) -> None:
        self.connector.destroy()
        self.type = None
        self.connector = None

    def prime_engine(self) -> None:
        self.connector.prime_engine()

    def get_active_config_id(self) -> int:
        return self.connector.get_active_config_id()

    def export_config(self) -> dict:
        return self.connector.export_config()

    def export_config_and_config_id(self) -> Tuple[dict,int]:
        return self.connector.export_config_and_config_id()

    def get_repository_last_modified_time(self) -> datetime:
        return self.connector.get_repository_last_modified_time()

    #Add records
    def add_record(self,
                   datasource_code: str,
                   record_id: str,
                   data_as_json: Union[str, dict],
                   load_id: str=None) -> None:
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if load_id:
            load_id = str(load_id)
        if isinstance(data_as_json, dict):
            data_as_json = json.dumps(data_as_json)
        self.connector.add_record(datasource_code=datasource_code, 
                                  record_id=record_id, 
                                  data_as_json=data_as_json, 
                                  load_id=load_id)

    def add_record_with_info_as_str(self,
                                    datasource_code: str,
                                    record_id: str,
                                    data_as_json: Union[str, dict],
                                    load_id: str=None,
                                    flags: Union[G2Flags, int]=None) -> str:
                                    #flags not currently used
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if load_id:
            load_id = str(load_id)
        if isinstance(data_as_json, dict):
            data_as_json = json.dumps(data_as_json)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        return self.connector.add_record_with_info(
            datasource_code=datasource_code,
            record_id=record_id,
            data_as_json=data_as_json,
            load_id=load_id,
            flags=flags)

    def add_record_with_info(self,
                             datasource_code: str,
                             record_id: str,
                             data_as_json: Union[str, dict],
                             load_id: str=None,
                             flags: Union[G2Flags, int]=None) -> dict:
        return json.loads(self.add_record_with_info_as_str(
            datasource_code=datasource_code,
            record_id=record_id,
            data_as_json=data_as_json,
            load_id=load_id,
            flags=flags
        ))


    def add_record_with_returned_record_id(self,
                                           datasource_code: str,
                                           data_as_json: Union[str,dict],
                                           load_id: str=None) -> str:
        datasource_code = str(datasource_code)
        if load_id:
            load_id = str(load_id)
        if isinstance(data_as_json, dict):
            data_as_json = json.dumps(data_as_json)
        return self.connector.add_record_with_returned_record_id(
            datasource_code=datasource_code,
            data_as_json=data_as_json,
            load_id=load_id)

    def add_record_with_info_with_returned_record_id_as_str(self,
                                                            datasource_code: str,
                                                            data_as_json: Union[str,dict],
                                                            load_id: str=None,
                                                            #flags not currently used
                                                            flags: Union[G2Flags,int]=None)\
                                                            -> Tuple[str, str]:
        datasource_code = str(datasource_code)
        if load_id:
            load_id = str(load_id)
        if isinstance(data_as_json, dict):
            data_as_json = json.dumps(data_as_json)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if not flags:
            flags = 0
        return self.connector.add_record_with_info_with_returned_record_id(
            datasource_code=datasource_code,
            data_as_json=data_as_json,
            load_id=load_id,
            flags=flags)

    def add_record_with_info_with_returned_record_id(self,
                                                     datasource_code: str,
                                                     data_as_json: Union[str,dict],
                                                     load_id: str=None,
                                                     flags: Union[G2Flags,int]=None)\
                                                     -> Tuple[dict, str]:
        retval = self.add_record_with_info_with_returned_record_id_as_str(
            datasource_code=datasource_code,
            data_as_json=data_as_json,
            load_id=load_id,
            flags=flags)
        return (json.loads(retval[0]), retval[1])

    #replace records
    def replace_record(self,
                       datasource_code: str,
                       record_id: str,
                       data_as_json: Union[str,dict],
                       load_id: bool=None):
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if load_id:
            load_id = str(load_id)
        if isinstance(data_as_json, dict):
            data_as_json = json.dumps(data_as_json)
        self.connector.replace_record(datasource_code=datasource_code,
                                      record_id=record_id,
                                      data_as_json=data_as_json,
                                      load_id=load_id)

    def replace_record_with_info_as_str(self,
                                        datasource_code,
                                        record_id,
                                        data_as_json,
                                        load_id=None,
                                        flags=None) -> str:
                                        #flags not currently used
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if load_id:
            load_id = str(load_id)
        if isinstance(data_as_json, dict):
            data_as_json = json.dumps(data_as_json)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        return self.connector.add_record_with_info(
            datasource_code=datasource_code, 
            record_id=record_id, 
            data_as_json=data_as_json, 
            load_id=load_id,
            flags=flags)

    def replace_record_with_info(self,
                                 datasource_code,
                                 record_id,
                                 data_as_json,
                                 load_id=None,
                                 flags=None):
                                 #flags not currently used
        retval = self.replace_record_with_info_as_str(
            datasource_code=datasource_code,
            record_id=record_id,
            data_as_json=data_as_json,
            load_id=load_id,
            flags=flags)
        return json.loads(retval)

    #reevaluation
    def reevaluate_record(self,
                          datasource_code: str,
                          record_id: str,
                          flags: G2Flags=G2EntityFlags()):
                          #is this the right flag?
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        self.connector.reevaluate_record(
            datasource_code=datasource_code,
            record_id=record_id,
            flags=flags)

    def reevaluate_record_with_info_as_str(self,
                                           datasource_code: str,
                                           record_id: str,
                                           flags: G2Flags=G2EntityFlags()) -> str:
                                           #is this the right flag?
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        result = self.connector.reevaluate_record_with_info(datasource_code=datasource_code, record_id=record_id, flags=flags)
        return result

    def reevaluate_record_with_info(self,
                                    datasource_code: str,
                                    record_id: str,
                                    flags: G2Flags=G2EntityFlags()) -> dict:
                                    #is this the right flag?
        retval = self.reevaluate_record_with_info_as_str(
            datasource_code=datasource_code,
            record_id=record_id,
            flags=flags)
        return json.loads(retval)

    def reevaluate_entity(self, entity_id: int, flags: G2Flags=None):
        entity_id = int(entity_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        self.connector.reevaluate_entity(entity_id=entity_id, flags=flags)

    def reevaluate_entity_with_info_as_str(self,
                                           entity_id: int,
                                           flags: G2Flags=G2EntityFlags())\
                                           -> str:
                                           #is this the right flag?
        entity_id = int(entity_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        result = self.connector.reevaluate_entity_with_info(
            entity_id=entity_id, 
            flags=flags)
        return result

    def reevaluate_entity_with_info(self,
                                    entity_id: int,
                                    flags: G2Flags=G2EntityFlags()):
        retval = self.reevaluate_entity_with_info_as_str(
            entity_id=entity_id,
            flags=flags)
        return json.loads(retval)

    #redo processing
    def count_redo_records(self) -> int:
        return self.connector.count_redo_records()

    def get_redo_record_as_str(self) -> str:
        result = self.connector.get_redo_record()
        #if there is no redo record, return None
        if len(result) == 0:
            return None
        return result

    def get_redo_record(self) -> dict:
        retval = self.get_redo_record_as_str()
        if not retval:
            return None
        return json.loads(self.get_redo_record_as_str())


    def process(self, redo_record: Union[str,dict]) -> None:
        if isinstance(redo_record, dict):
            redo_record = json.dumps(redo_record)
        self.connector.process(redo_record=redo_record)

    def process_with_info_as_str(self,
                                 redo_record: Union[str,dict],
                                 flags: G2Flags=G2EntityFlags()) -> str:
                                 #is this the right default?
        if isinstance(redo_record, dict):
            redo_record = json.dumps(redo_record)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        response = self.connector.process_with_info(redo_record, flags)
        return response

    def process_with_info(self,
                          redo_record: Union[str,dict],
                          flags: G2Flags=G2EntityFlags()) -> dict:
        retval = self.process_with_info_as_str(
            redo_record=redo_record,
            flags=flags)
        return json.loads(retval)


    def process_redo_record_as_str(self) -> str:
        response = self.connector.process_redo_record()
        return response

    def process_redo_record(self) -> dict:
        return json.loads(self.process_redo_record_as_str())

    def process_redo_record_with_info_as_str(self, 
                                             flags: G2Flags=G2EntityFlags()) -> Tuple[str,str]:
                                             #is this the right default?
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        (response, info) = self.connector.process_redo_record_with_info(flags)
        return (response, info)

    def process_redo_record_with_info(self,
                                      flags: G2Flags=G2EntityFlags()) -> Tuple[dict,dict]:
        retval = self.process_redo_record_with_info_as_str(flags=flags)
        return (json.loads(retval[0]), json.loads(retval[1]))


    #delete records
    def delete_record(self, datasource_code: str, record_id: str, load_id: str) -> None:
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        load_id = str(load_id)
        self.connector.delete_record(
            datasource_code=datasource_code,
            record_id=record_id,
            load_id=load_id)

    def delete_record_with_info_as_str(self,
                                       datasource_code: str,
                                       record_id: str,
                                       load_id: str=None,
                                       flags: G2Flags=G2RecordFlags())\
                                       -> str:
                                       #is this the right default?
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        load_id = str(load_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        response_info = self.connector.delete_record_with_info(
            datasource_code=datasource_code,
            record_id=record_id,
            load_id=load_id,
            flags=flags)
        return response_info

    def delete_record_with_info(self,
                                datasource_code: str,
                                record_id: str,
                                load_id: str=None,
                                flags: G2Flags=G2RecordFlags())\
                                -> dict:
        retval = self.delete_record_with_info_as_str(datasource_code=datasource_code,
                                                     record_id=record_id,
                                                     load_id=load_id,
                                                     flags=flags)
        return json.loads(retval)

    #get entity and records
    def get_record(self, 
                   datasource_code, 
                   record_id, 
                   flags=G2RecordFlags(), 
                   return_as_string=False):
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        record_info = self.connector.get_record(
            datasource_code, 
            record_id, 
            flags)
        if return_as_string:
            return record_info
        return json.loads(record_info)

    def get_entity_by_record_id(self, 
                                datasource_code, 
                                record_id, 
                                flags=G2EntityFlags(), 
                                return_as_string=False):
        datasource_code = str(datasource_code)
        record_id = str(record_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        entity_info = self.connector.get_entity_by_entity_id(
            datasource_code=datasource_code, 
            record_id=record_id, 
            flags=flags)
        if return_as_string:
            return entity_info
        return json.loads(entity_info)

    def get_entity_by_entity_id(self, 
                                entity_id, 
                                flags=G2EntityFlags(), 
                                return_as_string=False):
        entity_id = int(entity_id)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        entity_info = self.connector.get_entity_by_entity_id(
            entity_id=entity_id, 
            flags=flags)
        if return_as_string:
            return entity_info
        return json.loads(entity_info)

    #search 
    def search_by_attributes(self, 
                             search_attributes, 
                             flags=G2SearchByAttribtuesFlags(), 
                             return_as_string=False):
        if isinstance(search_attributes, dict):
            search_attributes = json.dumps(search_attributes)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if flags is None:
            flags = 0
        search_results = self.connector.search_by_attributes(
            search_attributes, 
            flags)
        if return_as_string:
            return search_results
        return json.loads(search_results)

    #find paths
    def find_path_by_entity_id(self,
                               start_entity_id,
                               end_entity_id,
                               max_degree,
                               flags=G2FindPathFlags(),
                               return_as_string=False):
        start_entity_id = int(start_entity_id)
        end_entity_id = int(end_entity_id)
        max_degree = int(max_degree)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        find_path_results = self.connector.find_path_by_entity_id(
            start_entity_id,
            end_entity_id,
            max_degree,
            flags)
        if return_as_string:
            return find_path_results
        return json.loads(find_path_results)

    def find_path_by_record_id(self,
                               start_datasource_code,
                               start_record_id,
                               end_datasource_code,
                               end_record_id,
                               max_degree,
                               flags=G2FindPathFlags(),
                               return_as_string=False):
        start_datasource_code = str(start_datasource_code)
        start_record_id =  str(start_record_id)
        end_datasource_code = str(end_datasource_code)
        end_record_id =  str(end_record_id)
        max_degree = int(max_degree)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        find_path_results = self.connector.find_path_by_record_id(
            start_datasource_code=start_datasource_code,
            start_record_id=start_record_id,
            end_datasource_code=end_datasource_code,
            end_record_id=end_record_id,
            max_degree=max_degree,
            flags=flags)
        if return_as_string:
            return find_path_results
        return json.loads(find_path_results)

    def find_path_excluding_by_entity_id(self,
                                         start_entity_id,
                                         end_entity_id,
                                         max_degree,
                                         excluded_entities,
                                         flags=G2FindPathFlags(),
                                         return_as_string=False):
        start_entity_id = int(start_entity_id)
        end_entity_id = int(end_entity_id)
        max_degree = int(max_degree)
        if isinstance(excluded_entities, dict):
            excluded_entities = json.dumps(excluded_entities)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        find_path_results = self.connector.find_path_excluding_by_entity_id(
            start_entity_id=start_entity_id,
            end_entity_id=end_entity_id,
            max_degree=max_degree,
            excluded_entities=excluded_entities,
            flags=flags)
        if return_as_string:
            return find_path_results
        return json.loads(find_path_results)

    def find_path_excluding_by_record_id(self,
                                         start_datasource_code,
                                         start_record_id,
                                         end_datasource_code,
                                         end_record_id,
                                         max_degree,
                                         excluded_entities,
                                         flags=G2FindPathFlags(),
                                         return_as_string=False):
        start_datasource_code = str(start_datasource_code)
        start_record_id =  str(start_record_id)
        end_datasource_code = str(end_datasource_code)
        end_record_id =  str(end_record_id)
        max_degree = int(max_degree)
        if isinstance(excluded_entities, dict):
            excluded_entities = json.dumps(excluded_entities)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        find_path_results = self.connector.find_path_excluding_by_record_id(
            start_datasource_code=start_datasource_code,
            start_record_id=start_record_id,
            end_datasource_code=end_datasource_code,
            end_record_id=end_record_id,
            max_degree=max_degree,
            excluded_entities=excluded_entities,
            flags=flags)
        if return_as_string:
            return find_path_results
        return json.loads(find_path_results)

    def find_path_including_source_by_entity_id(self,
                                                start_entity_id,
                                                end_entity_id,
                                                max_degree,
                                                excluded_entities,
                                                required_datasources,
                                                flags=G2FindPathFlags(),
                                                return_as_string=False):
        start_entity_id = int(start_entity_id)
        end_entity_id = int(end_entity_id)
        max_degree = int(max_degree)
        if isinstance(excluded_entities, dict):
            excluded_entities = json.dumps(excluded_entities)
        if isinstance(required_datasources, dict):
            required_datasources = json.dumps(required_datasources)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        find_path_results = self.connector.find_path_including_source_by_entity_id(
            start_entity_id=start_entity_id,
            end_entity_id=end_entity_id,
            max_degree=max_degree,
            excluded_entities=excluded_entities,
            required_datasources=required_datasources,
            flags=flags)
        if return_as_string:
            return find_path_results
        return json.loads(find_path_results)

    def find_path_including_source_by_record_id(self,
                                                start_datasource_code,
                                                start_record_id,
                                                end_datasource_code,
                                                end_record_id,
                                                max_degree,
                                                excluded_entities,
                                                required_datasources,
                                                flags=G2FindPathFlags(),
                                                return_as_string=False):
        start_datasource_code = str(start_datasource_code)
        start_record_id =  str(start_record_id)
        end_datasource_code = str(end_datasource_code)
        end_record_id =  str(end_record_id)
        max_degree = int(max_degree)
        if isinstance(excluded_entities, dict):
            excluded_entities = json.dumps(excluded_entities)
        if isinstance(required_datasources, dict):
            required_datasources = json.dumps(required_datasources)
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        find_path_results = self.connector.find_path_including_source_by_record_id(
            start_datasource_code=start_datasource_code,
            start_record_id=start_record_id,
            end_datasource_code=end_datasource_code,
            end_record_id=end_record_id,
            max_degree=max_degree,
            excluded_entities=excluded_entities,
            required_datasources=required_datasources,
            flags=flags)
        if return_as_string:
            return find_path_results
        return json.loads(find_path_results)

    #find networks
    def find_network_by_entity_id(self,
                                  entity_list,
                                  max_degree,
                                  buildout_degree,
                                  max_entities,
                                  flags=G2FindPathFlags(),
                                  #is this the right default?
                                  return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if isinstance(entity_list, dict):
            entity_list = json.dumps(entity_list)
        max_degree = int(max_degree)
        buildout_degree = int(buildout_degree)
        max_entities = int(max_entities)
        find_network_results = self.connector.find_network_by_entity_id(
            entity_list=entity_list,
            max_degree=max_degree,
            buildout_degree=buildout_degree,
            max_entities=max_entities,
            flags=flags)
        if return_as_string:
            return find_network_results
        return json.loads(find_network_results)

    def find_network_by_record_id(self, 
                                  record_list, 
                                  max_degree, 
                                  buildout_degree, 
                                  max_entities, 
                                  flags=G2FindPathFlags(), 
                                  #is this the right default?
                                  return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        if isinstance(record_list, dict):
            record_list = json.dumps(record_list)
        max_degree = int(max_degree)
        buildout_degree = int(buildout_degree)
        max_entities = int(max_entities)
        find_network_results = self.connector.find_network_by_record_id(
            record_list=record_list,
            max_degree=max_degree,
            buildout_degree=buildout_degree,
            max_entities=max_entities,
            flags=flags)
        if return_as_string:
            return find_network_results
        return json.loads(find_network_results)

    #why
    def why_entities(self, 
                     entity_id_1, 
                     entity_id_2, 
                     flags=G2WhyEntityFlags(), 
                     return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        entity_id_1 = int(entity_id_1)
        entity_id_2 = int(entity_id_2)
        why_result = self.connector.why_entities(
            entity_id_1, 
            entity_id_2, 
            flags)
        if return_as_string:
            return why_result
        return json.loads(why_result)

    def why_records(self, 
                    datasource_code_1, 
                    record_id_1, 
                    datasource_code_2, 
                    record_id_2, 
                    flags=G2WhyEntityFlags(), 
                    return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        datasource_code_1 = str(datasource_code_1)
        record_id_1 = str(record_id_1)
        datasource_code_2 = str(datasource_code_2)
        record_id_2 = str(record_id_2)
        why_result = self.connector.why_records(
            datasource_code_1,
            record_id_1,
            datasource_code_2,
            record_id_2,
            flags
        )
        if return_as_string:
            return why_result
        return json.loads(why_result)

    def why_entity_by_record_id(self,
                                datasource_code_1,
                                record_id_1,
                                flags=G2WhyEntityFlags(),
                                return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        datasource_code_1 = str(datasource_code_1)
        record_id_1 = str(record_id_1)
        why_result = self.connector.why_entity_by_record_id(
            datasource_code_1=datasource_code_1,
            record_id_1=record_id_1,
            flags=flags)
        if return_as_string:
            return why_result
        return json.loads(why_result)

    def why_entity_by_entity_id(self,
                                entity_id,
                                flags=G2WhyEntityFlags()):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        entity_id = int(entity_id)
        why_result = self.connector.why_entity_by_entity_id(
            entity_id=entity_id,
            flags=flags
        )

    def how_entity_by_entity_id(self, 
                                entity_id,
                                flags=G2HowEntityFlags(), 
                                return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        entity_id = int(entity_id)
        how_result = self.connector.how_entity_by_entity_id(
            entity_id,
            flags)
        if return_as_string:
            return how_result
        return json.loads(how_result)

    #export
    def export_csv_entity_report_with_callback(self, 
                                               columns, 
                                               callback, 
                                               flags=G2ExportFlags(), 
                                               return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        return self.connector.export_csv_entity_report_with_callback(
            columns,
            flags,
            callback,
            return_as_string)

    def export_csv_entity_report_iteritems(self, 
                                           columns, 
                                           flags=G2ExportFlags(), 
                                           return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        return self.connector.export_csv_entity_report_iteritems(
            columns,
            flags,
            return_as_string)

    def export_json_entity_report_with_callback(self, 
                                                callback, 
                                                flags=G2ExportFlags(), 
                                                return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        return self.connector.export_json_entity_report_with_callback(
            flags=flags,
            callback=callback,
            return_as_string=return_as_string)

    def export_json_entity_report_iteritems(self, 
                                            flags=G2ExportFlags(), 
                                            return_as_string=False):
        if isinstance(flags, G2Flags):
            flags=flags.get_flags()
        return self.connector.export_json_entity_report_iteritems(
            flags=flags,
            return_as_string=return_as_string)

    #purge
    def purge_repository(self):
        self.connector.purge_repository()

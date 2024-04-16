from .. import errors as errors
from ..utils.utils import (
    convert_port_bindings as convert_port_bindings,
    convert_tmpfs_mounts as convert_tmpfs_mounts,
    convert_volume_binds as convert_volume_binds,
    format_environment as format_environment,
    format_extra_hosts as format_extra_hosts,
    normalize_links as normalize_links,
    parse_bytes as parse_bytes,
    parse_devices as parse_devices,
    split_command as split_command,
    version_gte as version_gte,
    version_lt as version_lt,
)
from .base import DictType as DictType
from .healthcheck import Healthcheck as Healthcheck
from _typeshed import Incomplete

class LogConfigTypesEnum:
    JSON: Incomplete
    SYSLOG: Incomplete
    JOURNALD: Incomplete
    GELF: Incomplete
    FLUENTD: Incomplete
    NONE: Incomplete

class LogConfig(DictType):
    types = LogConfigTypesEnum
    def __init__(self, **kwargs) -> None: ...
    @property
    def type(self): ...
    @property
    def config(self): ...
    def set_config_value(self, key, value) -> None: ...
    def unset_config(self, key) -> None: ...

class Ulimit(DictType):
    def __init__(self, **kwargs) -> None: ...
    @property
    def name(self): ...
    @property
    def soft(self): ...
    @property
    def hard(self): ...

class DeviceRequest(DictType):
    def __init__(self, **kwargs) -> None: ...
    @property
    def driver(self): ...
    @property
    def count(self): ...
    @property
    def device_ids(self): ...
    @property
    def capabilities(self): ...
    @property
    def options(self): ...

class HostConfig(dict):
    def __init__(
        self,
        version,
        binds: Incomplete | None = ...,
        port_bindings: Incomplete | None = ...,
        lxc_conf: Incomplete | None = ...,
        publish_all_ports: bool = ...,
        links: Incomplete | None = ...,
        privileged: bool = ...,
        dns: Incomplete | None = ...,
        dns_search: Incomplete | None = ...,
        volumes_from: Incomplete | None = ...,
        network_mode: Incomplete | None = ...,
        restart_policy: Incomplete | None = ...,
        cap_add: Incomplete | None = ...,
        cap_drop: Incomplete | None = ...,
        devices: Incomplete | None = ...,
        extra_hosts: Incomplete | None = ...,
        read_only: Incomplete | None = ...,
        pid_mode: Incomplete | None = ...,
        ipc_mode: Incomplete | None = ...,
        security_opt: Incomplete | None = ...,
        ulimits: Incomplete | None = ...,
        log_config: Incomplete | None = ...,
        mem_limit: Incomplete | None = ...,
        memswap_limit: Incomplete | None = ...,
        mem_reservation: Incomplete | None = ...,
        kernel_memory: Incomplete | None = ...,
        mem_swappiness: Incomplete | None = ...,
        cgroup_parent: Incomplete | None = ...,
        group_add: Incomplete | None = ...,
        cpu_quota: Incomplete | None = ...,
        cpu_period: Incomplete | None = ...,
        blkio_weight: Incomplete | None = ...,
        blkio_weight_device: Incomplete | None = ...,
        device_read_bps: Incomplete | None = ...,
        device_write_bps: Incomplete | None = ...,
        device_read_iops: Incomplete | None = ...,
        device_write_iops: Incomplete | None = ...,
        oom_kill_disable: bool = ...,
        shm_size: Incomplete | None = ...,
        sysctls: Incomplete | None = ...,
        tmpfs: Incomplete | None = ...,
        oom_score_adj: Incomplete | None = ...,
        dns_opt: Incomplete | None = ...,
        cpu_shares: Incomplete | None = ...,
        cpuset_cpus: Incomplete | None = ...,
        userns_mode: Incomplete | None = ...,
        uts_mode: Incomplete | None = ...,
        pids_limit: Incomplete | None = ...,
        isolation: Incomplete | None = ...,
        auto_remove: bool = ...,
        storage_opt: Incomplete | None = ...,
        init: Incomplete | None = ...,
        init_path: Incomplete | None = ...,
        volume_driver: Incomplete | None = ...,
        cpu_count: Incomplete | None = ...,
        cpu_percent: Incomplete | None = ...,
        nano_cpus: Incomplete | None = ...,
        cpuset_mems: Incomplete | None = ...,
        runtime: Incomplete | None = ...,
        mounts: Incomplete | None = ...,
        cpu_rt_period: Incomplete | None = ...,
        cpu_rt_runtime: Incomplete | None = ...,
        device_cgroup_rules: Incomplete | None = ...,
        device_requests: Incomplete | None = ...,
        cgroupns: Incomplete | None = ...,
    ) -> None: ...

def host_config_type_error(param, param_value, expected): ...
def host_config_version_error(param, version, less_than: bool = ...): ...
def host_config_value_error(param, param_value): ...
def host_config_incompatible_error(param, param_value, incompatible_param): ...

class ContainerConfig(dict):
    def __init__(
        self,
        version,
        image,
        command,
        hostname: Incomplete | None = ...,
        user: Incomplete | None = ...,
        detach: bool = ...,
        stdin_open: bool = ...,
        tty: bool = ...,
        ports: Incomplete | None = ...,
        environment: Incomplete | None = ...,
        volumes: Incomplete | None = ...,
        network_disabled: bool = ...,
        entrypoint: Incomplete | None = ...,
        working_dir: Incomplete | None = ...,
        domainname: Incomplete | None = ...,
        host_config: Incomplete | None = ...,
        mac_address: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        stop_signal: Incomplete | None = ...,
        networking_config: Incomplete | None = ...,
        healthcheck: Incomplete | None = ...,
        stop_timeout: Incomplete | None = ...,
        runtime: Incomplete | None = ...,
    ) -> None: ...

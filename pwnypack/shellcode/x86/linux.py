from pwnypack.shellcode.types import NUMERIC, PTR, SyscallDef
from pwnypack.shellcode.linux import Linux
from pwnypack.shellcode.x86 import X86
from pwnypack.shellcode.x86.null_safe_mutable import X86NullSafeMutable


__all__ = ['LinuxX86', 'LinuxX86NullSafeMutable']


class LinuxX86(Linux, X86):
    """
    An environment that targets a generic Linux X86_64 machine.
    """

    sys_iopl = SyscallDef('sys_iopl', NUMERIC)  #:
    sys_vm86old = SyscallDef('sys_vm86old', PTR)  #:
    sys_sigreturn = SyscallDef('sys_sigreturn')  #:
    sys_modify_ldt = SyscallDef('sys_modify_ldt', NUMERIC, PTR, NUMERIC)  #:
    sys_vm86 = SyscallDef('sys_vm86', NUMERIC, NUMERIC)  #:
    sys_rt_sigreturn = SyscallDef('sys_rt_sigreturn')  #:
    sys_set_thread_area = SyscallDef('sys_set_thread_area', PTR)  #:
    sys_get_thread_area = SyscallDef('sys_get_thread_area', PTR)  #:

    SYSCALL_REG = X86.EAX
    SYSCALL_ARG_MAP = [X86.EBX, X86.ECX, X86.EDX, X86.ESI, X86.EDI]
    SYSCALL_RET_REG = X86.EAX
    SYSCALL_INSTR = 'int 0x80'
    SYSCALL_MAP = {
        Linux.sys_restart_syscall: 0,
        Linux.sys_exit: 1,
        Linux.sys_fork: 2,
        Linux.sys_read: 3,
        Linux.sys_write: 4,
        Linux.sys_open: 5,
        Linux.sys_close: 6,
        Linux.sys_waitpid: 7,
        Linux.sys_creat: 8,
        Linux.sys_link: 9,
        Linux.sys_unlink: 10,
        Linux.sys_execve: 11,
        Linux.sys_chdir: 12,
        Linux.sys_time: 13,
        Linux.sys_mknod: 14,
        Linux.sys_chmod: 15,
        Linux.sys_lchown16: 16,
        Linux.sys_stat: 18,
        Linux.sys_lseek: 19,
        Linux.sys_getpid: 20,
        Linux.sys_mount: 21,
        Linux.sys_oldumount: 22,
        Linux.sys_setuid16: 23,
        Linux.sys_getuid16: 24,
        Linux.sys_stime: 25,
        Linux.sys_ptrace: 26,
        Linux.sys_alarm: 27,
        Linux.sys_fstat: 28,
        Linux.sys_pause: 29,
        Linux.sys_utime: 30,
        Linux.sys_access: 33,
        Linux.sys_nice: 34,
        Linux.sys_sync: 36,
        Linux.sys_kill: 37,
        Linux.sys_rename: 38,
        Linux.sys_mkdir: 39,
        Linux.sys_rmdir: 40,
        Linux.sys_dup: 41,
        Linux.sys_pipe: 42,
        Linux.sys_times: 43,
        Linux.sys_brk: 45,
        Linux.sys_setgid16: 46,
        Linux.sys_getgid16: 47,
        Linux.sys_signal: 48,
        Linux.sys_geteuid16: 49,
        Linux.sys_getegid16: 50,
        Linux.sys_acct: 51,
        Linux.sys_umount: 52,
        Linux.sys_ioctl: 54,
        Linux.sys_fcntl: 55,
        Linux.sys_setpgid: 57,
        Linux.sys_olduname: 59,
        Linux.sys_umask: 60,
        Linux.sys_chroot: 61,
        Linux.sys_ustat: 62,
        Linux.sys_dup2: 63,
        Linux.sys_getppid: 64,
        Linux.sys_getpgrp: 65,
        Linux.sys_setsid: 66,
        Linux.sys_sigaction: 67,
        Linux.sys_sgetmask: 68,
        Linux.sys_ssetmask: 69,
        Linux.sys_setreuid16: 70,
        Linux.sys_setregid16: 71,
        Linux.sys_sigsuspend: 72,
        Linux.sys_sigpending: 73,
        Linux.sys_sethostname: 74,
        Linux.sys_setrlimit: 75,
        Linux.sys_old_getrlimit: 76,
        Linux.sys_getrusage: 77,
        Linux.sys_gettimeofday: 78,
        Linux.sys_settimeofday: 79,
        Linux.sys_getgroups16: 80,
        Linux.sys_setgroups16: 81,
        Linux.sys_old_select: 82,
        Linux.sys_symlink: 83,
        Linux.sys_lstat: 84,
        Linux.sys_readlink: 85,
        Linux.sys_uselib: 86,
        Linux.sys_swapon: 87,
        Linux.sys_reboot: 88,
        Linux.sys_old_readdir: 89,
        Linux.sys_old_mmap: 90,
        Linux.sys_munmap: 91,
        Linux.sys_truncate: 92,
        Linux.sys_ftruncate: 93,
        Linux.sys_fchmod: 94,
        Linux.sys_fchown16: 95,
        Linux.sys_getpriority: 96,
        Linux.sys_setpriority: 97,
        Linux.sys_statfs: 99,
        Linux.sys_fstatfs: 100,
        Linux.sys_ioperm: 101,
        Linux.sys_socketcall: 102,
        Linux.sys_syslog: 103,
        Linux.sys_setitimer: 104,
        Linux.sys_getitimer: 105,
        Linux.sys_newstat: 106,
        Linux.sys_newlstat: 107,
        Linux.sys_newfstat: 108,
        Linux.sys_uname: 109,
        sys_iopl: 110,
        Linux.sys_vhangup: 111,
        sys_vm86old: 113,
        Linux.sys_wait4: 114,
        Linux.sys_swapoff: 115,
        Linux.sys_sysinfo: 116,
        Linux.sys_ipc: 117,
        Linux.sys_fsync: 118,
        sys_sigreturn: 119,
        Linux.sys_clone: 120,
        Linux.sys_setdomainname: 121,
        Linux.sys_newuname: 122,
        sys_modify_ldt: 123,
        Linux.sys_adjtimex: 124,
        Linux.sys_mprotect: 125,
        Linux.sys_sigprocmask: 126,
        Linux.sys_init_module: 128,
        Linux.sys_delete_module: 129,
        Linux.sys_quotactl: 131,
        Linux.sys_getpgid: 132,
        Linux.sys_fchdir: 133,
        Linux.sys_bdflush: 134,
        Linux.sys_sysfs: 135,
        Linux.sys_personality: 136,
        Linux.sys_setfsuid16: 138,
        Linux.sys_setfsgid16: 139,
        Linux.sys_llseek: 140,
        Linux.sys_getdents: 141,
        Linux.sys_select: 142,
        Linux.sys_flock: 143,
        Linux.sys_msync: 144,
        Linux.sys_readv: 145,
        Linux.sys_writev: 146,
        Linux.sys_getsid: 147,
        Linux.sys_fdatasync: 148,
        Linux.sys_sysctl: 149,
        Linux.sys_mlock: 150,
        Linux.sys_munlock: 151,
        Linux.sys_mlockall: 152,
        Linux.sys_munlockall: 153,
        Linux.sys_sched_setparam: 154,
        Linux.sys_sched_getparam: 155,
        Linux.sys_sched_setscheduler: 156,
        Linux.sys_sched_getscheduler: 157,
        Linux.sys_sched_yield: 158,
        Linux.sys_sched_get_priority_max: 159,
        Linux.sys_sched_get_priority_min: 160,
        Linux.sys_sched_rr_get_interval: 161,
        Linux.sys_nanosleep: 162,
        Linux.sys_mremap: 163,
        Linux.sys_setresuid16: 164,
        Linux.sys_getresuid16: 165,
        sys_vm86: 166,
        Linux.sys_poll: 168,
        Linux.sys_setresgid16: 170,
        Linux.sys_getresgid16: 171,
        Linux.sys_prctl: 172,
        sys_rt_sigreturn: 173,
        Linux.sys_rt_sigaction: 174,
        Linux.sys_rt_sigprocmask: 175,
        Linux.sys_rt_sigpending: 176,
        Linux.sys_rt_sigtimedwait: 177,
        Linux.sys_rt_sigqueueinfo: 178,
        Linux.sys_rt_sigsuspend: 179,
        Linux.sys_pread64: 180,
        Linux.sys_pwrite64: 181,
        Linux.sys_chown16: 182,
        Linux.sys_getcwd: 183,
        Linux.sys_capget: 184,
        Linux.sys_capset: 185,
        Linux.sys_sigaltstack: 186,
        Linux.sys_sendfile: 187,
        Linux.sys_vfork: 190,
        Linux.sys_getrlimit: 191,
        Linux.sys_mmap_pgoff: 192,
        Linux.sys_truncate64: 193,
        Linux.sys_ftruncate64: 194,
        Linux.sys_stat64: 195,
        Linux.sys_lstat64: 196,
        Linux.sys_fstat64: 197,
        Linux.sys_lchown: 198,
        Linux.sys_getuid: 199,
        Linux.sys_getgid: 200,
        Linux.sys_geteuid: 201,
        Linux.sys_getegid: 202,
        Linux.sys_setreuid: 203,
        Linux.sys_setregid: 204,
        Linux.sys_getgroups: 205,
        Linux.sys_setgroups: 206,
        Linux.sys_fchown: 207,
        Linux.sys_setresuid: 208,
        Linux.sys_getresuid: 209,
        Linux.sys_setresgid: 210,
        Linux.sys_getresgid: 211,
        Linux.sys_chown: 212,
        Linux.sys_setuid: 213,
        Linux.sys_setgid: 214,
        Linux.sys_setfsuid: 215,
        Linux.sys_setfsgid: 216,
        Linux.sys_pivot_root: 217,
        Linux.sys_mincore: 218,
        Linux.sys_madvise: 219,
        Linux.sys_getdents64: 220,
        Linux.sys_fcntl64: 221,
        Linux.sys_gettid: 224,
        Linux.sys_readahead: 225,
        Linux.sys_setxattr: 226,
        Linux.sys_lsetxattr: 227,
        Linux.sys_fsetxattr: 228,
        Linux.sys_getxattr: 229,
        Linux.sys_lgetxattr: 230,
        Linux.sys_fgetxattr: 231,
        Linux.sys_listxattr: 232,
        Linux.sys_llistxattr: 233,
        Linux.sys_flistxattr: 234,
        Linux.sys_removexattr: 235,
        Linux.sys_lremovexattr: 236,
        Linux.sys_fremovexattr: 237,
        Linux.sys_tkill: 238,
        Linux.sys_sendfile64: 239,
        Linux.sys_futex: 240,
        Linux.sys_sched_setaffinity: 241,
        Linux.sys_sched_getaffinity: 242,
        sys_set_thread_area: 243,
        sys_get_thread_area: 244,
        Linux.sys_io_setup: 245,
        Linux.sys_io_destroy: 246,
        Linux.sys_io_getevents: 247,
        Linux.sys_io_submit: 248,
        Linux.sys_io_cancel: 249,
        Linux.sys_fadvise64: 250,
        Linux.sys_exit_group: 252,
        Linux.sys_lookup_dcookie: 253,
        Linux.sys_epoll_create: 254,
        Linux.sys_epoll_ctl: 255,
        Linux.sys_epoll_wait: 256,
        Linux.sys_remap_file_pages: 257,
        Linux.sys_set_tid_address: 258,
        Linux.sys_timer_create: 259,
        Linux.sys_timer_settime: 260,
        Linux.sys_timer_gettime: 261,
        Linux.sys_timer_getoverrun: 262,
        Linux.sys_timer_delete: 263,
        Linux.sys_clock_settime: 264,
        Linux.sys_clock_gettime: 265,
        Linux.sys_clock_getres: 266,
        Linux.sys_clock_nanosleep: 267,
        Linux.sys_statfs64: 268,
        Linux.sys_fstatfs64: 269,
        Linux.sys_tgkill: 270,
        Linux.sys_utimes: 271,
        Linux.sys_fadvise64_64: 272,
        Linux.sys_mbind: 274,
        Linux.sys_get_mempolicy: 275,
        Linux.sys_set_mempolicy: 276,
        Linux.sys_mq_open: 277,
        Linux.sys_mq_unlink: 278,
        Linux.sys_mq_timedsend: 279,
        Linux.sys_mq_timedreceive: 280,
        Linux.sys_mq_notify: 281,
        Linux.sys_mq_getsetattr: 282,
        Linux.sys_kexec_load: 283,
        Linux.sys_waitid: 284,
        Linux.sys_add_key: 286,
        Linux.sys_request_key: 287,
        Linux.sys_keyctl: 288,
        Linux.sys_ioprio_set: 289,
        Linux.sys_ioprio_get: 290,
        Linux.sys_inotify_init: 291,
        Linux.sys_inotify_add_watch: 292,
        Linux.sys_inotify_rm_watch: 293,
        Linux.sys_migrate_pages: 294,
        Linux.sys_openat: 295,
        Linux.sys_mkdirat: 296,
        Linux.sys_mknodat: 297,
        Linux.sys_fchownat: 298,
        Linux.sys_futimesat: 299,
        Linux.sys_fstatat64: 300,
        Linux.sys_unlinkat: 301,
        Linux.sys_renameat: 302,
        Linux.sys_linkat: 303,
        Linux.sys_symlinkat: 304,
        Linux.sys_readlinkat: 305,
        Linux.sys_fchmodat: 306,
        Linux.sys_faccessat: 307,
        Linux.sys_pselect6: 308,
        Linux.sys_ppoll: 309,
        Linux.sys_unshare: 310,
        Linux.sys_set_robust_list: 311,
        Linux.sys_get_robust_list: 312,
        Linux.sys_splice: 313,
        Linux.sys_sync_file_range: 314,
        Linux.sys_tee: 315,
        Linux.sys_vmsplice: 316,
        Linux.sys_move_pages: 317,
        Linux.sys_getcpu: 318,
        Linux.sys_epoll_pwait: 319,
        Linux.sys_utimensat: 320,
        Linux.sys_signalfd: 321,
        Linux.sys_timerfd_create: 322,
        Linux.sys_eventfd: 323,
        Linux.sys_fallocate: 324,
        Linux.sys_timerfd_settime: 325,
        Linux.sys_timerfd_gettime: 326,
        Linux.sys_signalfd4: 327,
        Linux.sys_eventfd2: 328,
        Linux.sys_epoll_create1: 329,
        Linux.sys_dup3: 330,
        Linux.sys_pipe2: 331,
        Linux.sys_inotify_init1: 332,
        Linux.sys_preadv: 333,
        Linux.sys_pwritev: 334,
        Linux.sys_rt_tgsigqueueinfo: 335,
        Linux.sys_perf_event_open: 336,
        Linux.sys_recvmmsg: 337,
        Linux.sys_fanotify_init: 338,
        Linux.sys_fanotify_mark: 339,
        Linux.sys_prlimit64: 340,
        Linux.sys_name_to_handle_at: 341,
        Linux.sys_open_by_handle_at: 342,
        Linux.sys_clock_adjtime: 343,
        Linux.sys_syncfs: 344,
        Linux.sys_sendmmsg: 345,
        Linux.sys_setns: 346,
        Linux.sys_process_vm_readv: 347,
        Linux.sys_process_vm_writev: 348,
        Linux.sys_kcmp: 349,
        Linux.sys_finit_module: 350,
        Linux.sys_sched_setattr: 351,
        Linux.sys_sched_getattr: 352,
        Linux.sys_renameat2: 353,
        Linux.sys_seccomp: 354,
        Linux.sys_getrandom: 355,
        Linux.sys_memfd_create: 356,
        Linux.sys_bpf: 357,
        Linux.sys_execveat: 358,
        Linux.sys_socket: 359,
        Linux.sys_socketpair: 360,
        Linux.sys_bind: 361,
        Linux.sys_connect: 362,
        Linux.sys_listen: 363,
        Linux.sys_accept4: 364,
        Linux.sys_getsockopt: 365,
        Linux.sys_setsockopt: 366,
        Linux.sys_getsockname: 367,
        Linux.sys_getpeername: 368,
        Linux.sys_sendto: 369,
        Linux.sys_sendmsg: 370,
        Linux.sys_recvfrom: 371,
        Linux.sys_recvmsg: 372,
        Linux.sys_shutdown: 373,
        Linux.sys_userfaultfd: 374,
        Linux.sys_membarrier: 375,
        Linux.sys_mlock2: 376,
        Linux.sys_copy_file_range: 377,
    }


class LinuxX86NullSafeMutable(X86NullSafeMutable, LinuxX86):
    """
    An environment that targets a Linux X86_32 machine in a writable segment
    that emits no NUL bytes or carriage return characters.
    """

---
  gather_facts: true
  become: yes

  vars:
    cis_level_1_exclusions:
      - 5.4.4
      - 3.4.2
      - 3.4.3
      - 6.2.13
    cis_pass_max_days: 45
    cis_umask_default: 002

  roles:
    - Ansible-RHEL7-CIS-Benchmarks/tasks/hot

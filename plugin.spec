---
config:
    plugin_type: other
subparsers:
    ir_plugin:
        description: InfraRed Plugin for Testing & POC Purposes
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Main Func
              options:
                  MBO1:
                      type: Bool
                      help: Master Branch - Option 1
                      default: False
                  B1O1:
                      type: Bool
                      help: B1 - Option 1
                      default: False


from eventhandlers.action_runners.ExportActionRunner import ExportActionRunner
from eventhandlers.action_runners.TaskTemplateActionRunner import TaskTemplateActionRunner
from enum import Enum


ACTION_RUNNERS_KIND_MAPPER = {
    'create_task': TaskTemplateActionRunner,
    'export': ExportActionRunner,
}

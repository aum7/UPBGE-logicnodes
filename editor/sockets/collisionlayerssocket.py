from .socket import NodeSocketLogic
from .socket import PARAM_LIST_SOCKET_COLOR
from .socket import socket_type
from bpy.props import BoolProperty
from bpy.types import NodeSocket


@socket_type
class NodeSocketLogicCollisionLayers(NodeSocket, NodeSocketLogic):
    bl_idname = "NLCollisionMaskSocket"
    bl_label = "Parameter"
    slot_0: BoolProperty(default=True)
    slot_1: BoolProperty(default=True)
    slot_2: BoolProperty(default=True)
    slot_3: BoolProperty(default=True)
    slot_4: BoolProperty(default=True)
    slot_5: BoolProperty(default=True)
    slot_6: BoolProperty(default=True)
    slot_7: BoolProperty(default=True)
    slot_8: BoolProperty(default=True)
    slot_9: BoolProperty(default=True)
    slot_10: BoolProperty(default=True)
    slot_11: BoolProperty(default=True)
    slot_12: BoolProperty(default=True)
    slot_13: BoolProperty(default=True)
    slot_14: BoolProperty(default=True)
    slot_15: BoolProperty(default=True)

    def draw_color(self, context, node):
        return PARAM_LIST_SOCKET_COLOR

    def draw(self, context, layout, node, text):
        if self.is_linked or self.is_output:
            layout.label(text=text)
        else:
            col = layout.column(align=True)
            col.scale_y = .8
            row = col.row(align=True)
            row2 = col.row(align=True)
            idx = 0
            while idx < 8:
                row.prop(self, f'slot_{idx}', text='',
                         emboss=True, icon='BLANK1')
                idx += 1
            while idx < 16:
                row2.prop(self, f'slot_{idx}', text='',
                          emboss=True, icon='BLANK1')
                idx += 1

    def get_unlinked_value(self):
        slots = [self.get(f'slot_{idx}', 1) * (2**idx) for idx in range(16)]
        return sum(slots)

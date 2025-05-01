# safety.py
import numpy as np

class SafetyLayer:
    def __init__(self, torque_limit):
        self.torque_limit = torque_limit

    def apply(self, action, current_torque):
        """安全规则示例：当伪扭矩过高时切换动作"""
        if current_torque > 0.8 * self.torque_limit:
            return 1 - action  # 切换动作（CartPole只有0和1）
        return action
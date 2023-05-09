import threading
from threading import Thread
import asyncio


class Arm:

    def __init__(self, arm_base, shoulder, elbow, wrist, twist_wrist, claw):
        self.arm_base = arm_base
        self.shoulder = shoulder
        self.elbow = elbow
        self.wrist = wrist
        self.twist_wrist = twist_wrist
        self.claw = claw
        self.threads = []

    async def rest(self):
        self.threads = [
            threading.Thread(target=self.shoulder.move_to, args=[0]),  # Creating threads
            threading.Thread(target=self.elbow.move_to, args=[180]),
            threading.Thread(target=self.wrist.move_to, args=[0])
        ]

        self.execute_actions()

    async def wake(self):
        self.threads = [
            threading.Thread(target=self.shoulder.move_to, args=[90]),  # Creating threads
            threading.Thread(target=self.elbow.move_to, args=[0]),
            threading.Thread(target=self.wrist.move_to, args=[90])
        ]

        self.execute_actions()

    async def stretch(self):
        self.threads = [
            threading.Thread(target=self.shoulder.move_to, args=[90]),  # Creating threads
            threading.Thread(target=self.elbow.move_to, args=[30]),
            threading.Thread(target=self.wrist.move_to, args=[25])
        ]

        self.execute_actions()

    def execute_actions(self):
        for th in self.threads:
            th.start()  # Starts the thread

        for th in self.threads:
            th.join()  # Waits for the thread to terminate

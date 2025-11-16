#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Transition - Enhanced with Stinger totalRate
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict

class Transition():
    class Dip():
        def __init__(self): # Transition.Dip
            self.input: ATEMConstant = ATEMConstant()
            self.rate: int = 0


    class DVE():
        def __init__(self): # Transition.DVE
            self.clip: float = 0.0
            self.enableKey: bool = False
            self.fillSource: ATEMConstant = ATEMConstant()
            self.flipFlop: bool = False
            self.gain: float = 0.0
            self.invertKey: bool = False
            self.keySource: ATEMConstant = ATEMConstant()
            self.preMultiplied: bool = False
            self.rate: int = 0
            self.reverse: bool = False
            self.style: ATEMConstant = ATEMConstant()


    class Mix():
        def __init__(self): # Transition.Mix
            self.rate: int = 0


    class Preview():
        def __init__(self): # Transition.Preview
            self.enabled: bool = False


    class Stinger():
        def __init__(self): # Transition.Stinger
            self.clip: float = 0.0
            self.clipDuration: int = 0
            self.gain: float = 0.0
            self.invertKey: bool = False
            self.mixRate: int = 0
            self.preMultiplied: bool = False
            self.preRoll: int = 0
            self.source: ATEMConstant = ATEMConstant()
            self.triggerPoint: int = 0

        @property
        def totalRate(self) -> int:
            """
            Get the total sting rate (mix rate + clip duration)
            This matches what ATEM software control displays in the rate field
            
            Returns:
                int: Total transition time in frames (mixRate + clipDuration)
            """
            return self.preRoll + self.clipDuration

        @property
        def stingRate(self) -> int:
            """
            Alias for totalRate - total sting duration including mix and clip
            This matches ATEM software behavior where the rate field shows total time
            
            Returns:
                int: Total transition time in frames (mixRate + clipDuration)
            """
            return self.totalRate

        @property
        def totalRateSeconds(self) -> float:
            """
            Get the total sting rate in seconds (assuming 25fps)
            
            Returns:
                float: Total transition time in seconds
            """
            return self.totalRate / 25.0

        def __str__(self) -> str:
            """String representation showing all sting parameters"""
            return (f"Stinger(mixRate={self.mixRate}, clipDuration={self.clipDuration}, "
                   f"totalRate={self.totalRate}, source={self.source}, "
                   f"triggerPoint={self.triggerPoint})")


    class Wipe():
        class Position():
            def __init__(self): # Transition.Wipe.Position
                self.x: float = 0.0
                self.y: float = 0.0


        def __init__(self): # Transition.Wipe
            self.fillSource: ATEMConstant = ATEMConstant()
            self.flipFlop: bool = False
            self.pattern: ATEMConstant = ATEMConstant()
            self.position: Transition.Wipe.Position = Transition.Wipe.Position()
            self.rate: int = 0
            self.reverse: bool = False
            self.softness: float = 0.0
            self.symmetry: float = 0.0
            self.width: float = 0.0


    class Next():
        def __init__(self): # Transition.Next
            self.background: bool = False
            self.key1: bool = False
            self.key2: bool = False
            self.key3: bool = False
            self.key4: bool = False



    def __init__(self): # Transition
        self.dip: Transition.Dip = Transition.Dip()
        self.dVE: Transition.DVE = Transition.DVE()
        self.framesRemaining: int = 0
        self.mix: Transition.Mix = Transition.Mix()
        self.preview: Transition.Preview = Transition.Preview()
        self.stinger: Transition.Stinger = Transition.Stinger()
        self.wipe: Transition.Wipe = Transition.Wipe()
        self.inTransition: bool = False
        self.position: int = 0
        self.style: ATEMConstant = ATEMConstant()
        self.nextTransition: Transition.Next = Transition.Next()
        self.styleNext: ATEMConstant = ATEMConstant()
        self.nextTransitionNext: Transition.Next = Transition.Next()


class TransitionList(ATEMValueDict[Transition]):
    def __init__(self): # TransitionList
        super().__init__(Transition, ATEMProtocol.mixEffects)

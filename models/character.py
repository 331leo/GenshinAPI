from enum import Enum
from typing import List

from pydantic import BaseModel, Field, HttpUrl
from pydantic.types import conint


class CharacterElements(str, Enum):
    Pyro = "Pyro"
    Hydro = "Hydro"
    Anemo = "Anemo"
    Electro = "Electro"
    Dendro = "Dendro"
    Cyro = "Cryo"
    Geo = "Geo"


class ArtifactPosition(str, Enum):
    Flower = "flower"
    Feather = "feather"
    Hourglass = "hourglass"
    Goblet = "goblet"
    Crown = "crown"


class CharacterWeapon(BaseModel):
    name: str = Field(description="Attached weapon (장착된 무기)", example="용의 포효")
    rarity: conint(ge=1, le=5) = Field(description="Weapon rarity (무기 희귀도)", example=4)
    type: str = Field(description="Weapon type (무기 종류)", example="한손검")
    level: int = Field(description="Weapon level (무기 레벨)", example=50)
    ascension: int = Field(description="Weapon ascension level (무기 돌파 레벨", example=2)
    refinement: int = Field(description="Weapon refinement level (무기 제련 단계)", example=1)
    description: str = Field(
        description="Weapon in-game description (무기 인게임 설명)",
        example="조각 문양은 조금 과장된 느낌이 있지만 검의 유연도와 예리함은 손색이 없다. 공기를 가를 때 용의 포효가 들리는 듯하다",
    )
    icon: str = Field(
        description="Weapon icon image url (무기 아이콘 URL)",
        example="https://upload-os-bbs.mihoyo.com/game_record/genshin/equip/UI_EquipIcon_Sword_Rockkiller.png",
    )


class CharacterArtifact(BaseModel):
    name: str = Field(description="Artifact Name (성유물 이름)", example="전쟁광의 장미")
    pos_name: ArtifactPosition = Field(
        description="Artifact position (성유물 종류)", example=ArtifactPosition.Flower
    )
    rarity: conint(ge=1, le=5) = Field(
        description="Artifact rarity (성유물 희귀도)", example=5
    )
    level: int = Field(description="Artifact level (성유물 레벨)", example=6)
    icon: str = Field(
        description="Artifact icon url (성유물 아이콘 URL)",
        example="https://upload-os-bbs.mihoyo.com/game_record/genshin/equip/UI_RelicIcon_10005_4.png",
    )


class Character(BaseModel):
    name: str = Field(description="Character Name (캐릭터 이름)", example="각청")
    rarity: conint(ge=1, le=5) = Field(
        description="Character rarity (캐릭터 희귀도)", example=5
    )
    element: CharacterElements = Field(
        description="Character element (캐릭터 원소 특성)", example=CharacterElements.Electro
    )
    level: int = Field(description="Character level (캐릭터 레벨)", example=80)
    friendship: int = Field(
        description="Character friendship level (캐릭터 호감도 레벨)", example=2
    )
    constellation: int = Field(
        description="Character opened constellation (해금된 운명의 자리)", example=1
    )
    icon: str = Field(
        description="Character icon url (캐릭터 아이콘 URL)",
        example="https://upload-os-bbs.mihoyo.com/game_record/genshin/character_icon/UI_AvatarIcon_Keqing.png",
    )
    image: str = Field(
        description="Character full image url (캐릭터 이미지 URL)",
        example="https://upload-os-bbs.mihoyo.com/game_record/genshin/character_image/UI_AvatarIcon_Keqing@2x.png",
    )
    weapon: CharacterWeapon
    artifacts: List[CharacterArtifact]

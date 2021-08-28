from pydantic import BaseModel, Field


class Stats(BaseModel):
    achievements: int = Field(
        description="Number of achievements (업적 달성 개수)", example=54
    )
    active_days: int = Field(description="Number of active days (활동일수)", example=365)
    characters: int = Field(
        description="Number of earned characters (획득한 캐릭터 개수)", example=6
    )
    spiral_abyss: str = Field(
        description="Progress of spiral abyss (나선 비경 진도)", example="6-2"
    )
    anemoculi: int = Field(
        description="Number of earned Anemoculus (수집한 바람 신의 눈동자)", example=40
    )
    geoculi: int = Field(
        description="Number of earned Geoculus (수집한 바위 신의 눈동자)", example=39
    )
    electroculi: int = Field(
        description="Number of earned Electroculus (수집한 번개 신의 눈동자)", example=12
    )
    common_chests: int = Field(
        description="Opened common chests (수집한 평범한 보물상자 개수)", example=89
    )
    exquisite_chests: int = Field(
        description="Opened excelcise chests (수집한 정교한 보물상자 개수)", example=98
    )
    precious_chests: int = Field(
        description="Opened precious chests (수집한 진귀한 보물상자 개수)", example=23
    )
    luxurious_chests: int = Field(
        description="Opened luxurious chests (수집한 화려한 보물상자 개수)", example=7
    )
    unlocked_waypoints: int = Field(
        description="Unlocked waypoints (활성화된 워프포인트)", example=85
    )
    unlocked_domains: int = Field(description="Unlocked domains (개방된 비경)", example=19)

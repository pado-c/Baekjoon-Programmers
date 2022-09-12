-- 코드를 입력하세요
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS as INS
INNER JOIN ANIMAL_OUTS as OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE != OUTS.SEX_UPON_OUTCOME
SELECT "REG_ANS", SUM(COALESCE("VL_SALDO", 0)) AS total_despesas
FROM public."4T2024"
GROUP BY "REG_ANS"
ORDER BY total_despesas DESC
LIMIT 10;

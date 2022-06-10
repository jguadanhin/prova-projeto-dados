import pandas as pd

ingressos = {"ano":2020,"dia":1,"mes":1,"nome":"Benjamin Mcdonald","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Mitchell Kostyla","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Gerald Allen","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Frederick Bank","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Tina Yee","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Ruth Ridge","status":"Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Jeffrey Pace","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Nicholas Johansson","status":"Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"William Barnes","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Charles Hershenson","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Edna Martinez","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Lyle Branch","status":"Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Deborah Silsby","status":"Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Nancy Smith","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Donna Chandler","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"John Rich","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"John Rich","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Maria Marshall","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Tina Yee","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Felicia Hallman","status":"Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Guadalupe Bell","status":"Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Shayla Baird","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Kelly Williamson","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Edna Martinez","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"James Coffey","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Frances Lambert","status":"Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Matt Smudrick","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":2,"mes":1,"nome":"Alice Gamba","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":3,"mes":1,"nome":"Tina Yee","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":3,"mes":1,"nome":"John Rich","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":3,"mes":1,"nome":"Larry Teague","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":3,"mes":1,"nome":"Andrea Galyen","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":3,"mes":1,"nome":"Yong Baltazar","status":"Nao Concluido","tipo":"VIP"},{"ano":2020,"dia":3,"mes":1,"nome":"Elizabeth Daly","status":"Problema no Pagamento","tipo":"VIP"},{"ano":2020,"dia":1,"mes":1,"nome":"Joshua Sanderson","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Donna Wal","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Andrea Galyen","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Lyle Branch","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Debra Howard","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Debra Howard","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Daniel Puckett","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Gretchen Hinojosa","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Suzanne Herring","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Jarrod Adler","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Gretchen Hinojosa","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Travis Whatley","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"Elizabeth Daly","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":2,"mes":1,"nome":"Lyle Branch","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":2,"mes":1,"nome":"Emil Nord","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":2,"mes":1,"nome":"John Rich","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":2,"mes":1,"nome":"James Reaves","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":2,"mes":1,"nome":"Frank Houck","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":2,"mes":1,"nome":"John Rich","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":2,"mes":1,"nome":"Courtney Edwards","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Richard Culpepper","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Young Besaw","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Lucia Hayes","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Kelly Williamson","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Marcela Nelson","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Sandra Duncan","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Miguel Ramey","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Nancy Degroot","status":"Nao Concluido","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Edward Smith","status":"Problema no Pagamento","tipo":"Pista"},{"ano":2020,"dia":3,"mes":1,"nome":"Mitchell Kostyla","status":"Concluido","tipo":"Pista"},{"ano":2020,"dia":1,"mes":1,"nome":"John Rich","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Clara Faupel","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Blanche Knox","status":"Nao Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Michael Gaines","status":"Nao Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Maria Villa","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Ricardo Clasby","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"James Reaves","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Richard Culpepper","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Frank Houck","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Courtney Edwards","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Tina Yee","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Pamela Nixon","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":1,"mes":1,"nome":"Brenda Key","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Frederick Bank","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Frank Davilla","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Mitchell Kostyla","status":"Nao Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"James Reaves","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Sabrina Graves","status":"Nao Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Kathleen Duncan","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Richard Culpepper","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Margaret Robinson","status":"Nao Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Rick Fleishman","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Linda Batiz","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Michael Gaines","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":2,"mes":1,"nome":"Amy Mejia","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"John Rich","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"John Rich","status":"Nao Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Donna Wal","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Joseph Wray","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Barbara Mcneil","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Eduardo Espenshade","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Richard Jimenez","status":"Nao Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Curtis Hernandez","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Alice Gamba","status":"Concluido","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Brenda Kozak","status":"Problema no Pagamento","tipo":"Pista Premium"},{"ano":2020,"dia":3,"mes":1,"nome":"Robert Copenhaver","status":"Concluido","tipo":"Pista Premium"}
di = pd.DataFrame(data=ingressos)

di.to_excel('ingressos.xlsx')






insert into `responsable` (`id`, `nom`, `service`, `embauche`) values (NULL, 'Massonniere', 'IMIE', '2020-01-01');

insert into `fabricant` (`id`, `nom`) values (NULL, 'Massonniere Company');

insert into `materiel` (`id`, `nom`, `description`, `dateInstallation`, `id_Fabricant`, `id_Responsable`) values (NULL, 'Console', 'Sony PlayStation 4 Slim 1 To + FIFA 20 + PS Plus', '2024-10-23', '8', '8');

select * from responsable order by embauche asc limit 1;

select r.* from responsable r inner join materiel m on r.id = m.id_Responsable where m.nom = "Serveur";

select m.nom, r.nom from responsable r inner join materiel m on r.id = m.id_Responsable group by m.nom;

select f.nom, count(m.nom) from materiel m inner join fabricant f on m.id_fabricant = f.id group by f.nom;

select r.nom, m.nom, m.dateInstallation, f.nom from responsable r inner join materiel m on r.id = m.id_Responsable inner join fabricant f on f.id = m.id_Fabricant;

delimiter $
drop procedure if exists getHardwareByYear$
create procedure getHardwareByYear(in year varchar(4))
begin
    select m.nom, f.nom, r.nom from responsable r inner join materiel m on r.id = m.id_Responsable inner join fabricant f on f.id = m.id_Fabricant where dateInstallation like concat('%', year, '%');
end$
delimiter ;
call getHardwareByYear("2020");
call getHardwareByYear("2013");
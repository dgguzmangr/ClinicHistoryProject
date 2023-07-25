package VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Modelos.Rol;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}

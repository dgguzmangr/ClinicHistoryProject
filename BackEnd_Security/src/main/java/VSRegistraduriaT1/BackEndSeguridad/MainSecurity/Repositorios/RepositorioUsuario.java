package VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Repositorios;

import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioUsuario extends MongoRepository<Usuario, String> {
    @Query("{'correo':?0}")
    Usuario getUserByMail(String correo);
}

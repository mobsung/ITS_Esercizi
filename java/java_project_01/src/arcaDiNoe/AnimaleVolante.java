package arcaDiNoe;

public abstract class AnimaleVolante implements Animale {
	
	private final String categoria = "animale volante";
	
	public String categoria() {
		return categoria;
	}

	@Override
	public String toString() {
		return "categoria=" + categoria;
	}
	
	
}

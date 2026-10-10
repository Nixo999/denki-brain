/** A che punto è un lavoro secondo Haiku. Il piano di TodoWrite, quando c'è, vince e non passa di qui. */
export type Stima = {
  pct: number
  /** Cosa sta facendo adesso, in poche parole. */
  fase: string
  /** Solo per la chat: il compito principale, in una riga. */
  obiettivo?: string
  /** Quanti passi o messaggi c'erano quando è stata fatta: se non cambiano non si rifà. */
  passi: number
  quando: number
}

declare module 'claude-code' {
  interface PluginState {
    'agenti-live': {
      /** Batte ogni 5 secondi: chi lo legge si ridisegna. */
      tick: number
      /** Per id dell'agente, e `main` per la chat. */
      stime: Record<string, Stima>
    }
  }
}

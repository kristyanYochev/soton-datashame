import { Pages } from "./enums";

export interface SharedProps { 
  setPage: (val: Pages) => void;
}
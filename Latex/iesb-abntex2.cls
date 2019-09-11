%%
%% Customizações do abnTeX2 (http://abnTeX2.googlecode.com) para o Centro Universitário IESB
%%
%% This work may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%   http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2005/12/01 or later.
%%
%% This work has the LPPL maintenance status `maintained'.
%% 
%% The Current Maintainer of this work is ÊNIO JOSÉ FERREIRA JÚNIOR, juniorr452@gmail.com
%%
%% Further information about abnTeX2 are available on http://abntex2.googlecode.com/
%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{iesb-abntex2}[2019/02/22 v1.0 Modelo do Centro Universitário IESB baseado em abnTeX2]

%
% Repassa todos os parametros a classe abntex2, 
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{abntex2}%
}
\ProcessOptions\relax
\LoadClass{abntex2}
\usepackage[utf8]{inputenc}

\newcommand{\IESBheader}{
    \noindent\begin{minipage}{0.2\textwidth}% adapt widths of minipages to your needs
    \raggedleft
    \includegraphics[scale=0.4]{iesb.png}
    \end{minipage}%
    \hfill
    \begin{minipage}{0.8\textwidth}
    \ABNTEXchapterfont\large\textbf{CENTRO UNIVERSITÁRIO IESB} 
    \hr\par
    \ABNTEXchapterfont\large\textbf{Centro Universitário Instituto de Educação Superior de Brasília} 
    \hr
    \end{minipage}
    
}

% alterando a capa
\renewcommand{\imprimircapa}{%
  \begin{capa}%
    \center
    \IESBheader
    
    \vspace*{1cm}
    
    {\ABNTEXchapterfont\large\imprimirautor}

    \vfill
    \begin{center}
    \ABNTEXchapterfont\bfseries\LARGE\imprimirtitulo
    \end{center}
    \vfill
    
    \large\imprimirlocal

    \large\imprimirdata
    
    \vspace*{1cm}
  \end{capa}
}


% folha de rosto 

\makeatletter

\renewcommand{\folhaderostocontent}{
\begin{center}{\IESBheader}
    
    \vspace*{1cm}
    
{\ABNTEXchapterfont\large\imprimirautor}

\vspace*{\fill}\vspace*{\fill}

\begin{center}
\ABNTEXchapterfont\bfseries\Large\imprimirtitulo
\end{center}

\vspace*{\fill}

\abntex@ifnotempty{\imprimirpreambulo}{%
  \hspace{.45\textwidth}
  \begin{minipage}{.5\textwidth}
  \SingleSpacing
  \imprimirpreambulo
  \end{minipage}%
  \vspace*{\fill}
}%

{\large\imprimirorientadorRotulo~\imprimirorientador\par}

\abntex@ifnotempty{\imprimircoorientador}{%
  {\large\imprimircoorientadorRotulo~\imprimircoorientador}%
}%

\vspace*{\fill}

{\abntex@ifnotempty{\imprimirinstituicao}{\imprimirinstituicao\vspace*{\fill}}}

{\large\imprimirlocal}

\par

\titulo

{\large\imprimirdata}
\vspace*{1cm}
\end{center}
}

\makeatother

% --- 
% Espaçamentos entre linhas e parágrafos 
% --- 

% O tamanho do parágrafo é dado por:
\setlength{\parindent}{1.5cm}

% Controle do espaçamento entre um parágrafo e outro:
\setlength{\parskip}{0.2cm}  % tente também \onelineskip

\newcommand\hr{\par\vspace{-.9\ht\strutbox}\noindent\color{red}\hrulefill\color{black}
}

\renewcommand{\rmdefault}{phv} % Arial
\renewcommand{\sfdefault}{phv} % Arial

\newcommand{\imprimircurso}{Ciência da Computação\par}
\newcommand{\imprimirdataapresentacao}{25 de dezembro de 2019}

\interfootnotelinepenalty=10000